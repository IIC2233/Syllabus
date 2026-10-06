const resultEl = document.getElementById('result');
const statusEl = document.getElementById('status');
const baseUrlEl = document.getElementById('base-url');
const tokenEl = document.getElementById('auth-token');
const gamesGridEl = document.getElementById('games-grid');
const genresListEl = document.getElementById('genre-list');
const libraryMetaEl = document.getElementById('library-meta');
const compareWinnerEl = document.getElementById('compare-winner');
const featuredCoverEl = document.getElementById('featured-cover');
const featuredTitleEl = document.getElementById('featured-title');
const featuredDescriptionEl = document.getElementById('featured-description');
const featuredTagsEl = document.getElementById('featured-tags');
const featuredRatingEl = document.getElementById('featured-rating');
const featuredHoursEl = document.getElementById('featured-hours');
const featuredPriceEl = document.getElementById('featured-price');

const state = {
  allGames: [],
  shownGames: [],
  activeGenre: 'Todos'
};

function getBaseUrl() {
  return (baseUrlEl.value || '').trim();
}

function buildUrl(path) {
  const base = getBaseUrl();
  if (!base) return path;
  return `${base.replace(/\/$/, '')}${path}`;
}

function showResult(ok, method, path, status, data) {
  statusEl.textContent = `${method} ${path} -> HTTP ${status}`;
  statusEl.className = `status ${ok ? 'ok' : 'error'}`;
  resultEl.textContent = JSON.stringify(data, null, 2);
}

function commaListToArray(input) {
  return input
    .split(',')
    .map((item) => item.trim())
    .filter(Boolean);
}

function formatMoney(price) {
  return Number(price) === 0 ? 'Free to Play' : `$${price}`;
}

function prettyGameName(name) {
  return name
    .split('_')
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ');
}

function getCardGradient(id) {
  const variants = [
    'linear-gradient(145deg, #326ea1, #16253d)',
    'linear-gradient(145deg, #2b8d8b, #0e2e38)',
    'linear-gradient(145deg, #7a4ca1, #22173d)',
    'linear-gradient(145deg, #85662b, #2b2010)',
    'linear-gradient(145deg, #9b4a5a, #2d141f)'
  ];
  return variants[id % variants.length];
}

function requireAtLeastOne(values) {
  return values.some((value) => value !== undefined && value !== null && value !== '' && value !== 0);
}

async function apiFetch(path, options = {}, useAuth = false) {
  const headers = {
    'Content-Type': 'application/json',
    ...(options.headers || {})
  };

  if (useAuth) {
    headers.Authorization = tokenEl.value.trim();
  }

  const method = options.method || 'GET';
  try {
    const response = await fetch(buildUrl(path), {
      ...options,
      headers
    });

    let data;
    try {
      data = await response.json();
    } catch {
      data = { error: 'Respuesta no JSON' };
    }

    showResult(response.ok, method, path, response.status, data);
    return { response, data };
  } catch {
    const data = { error: 'No se pudo conectar con la API' };
    showResult(false, method, path, 0, data);
    return { response: { ok: false, status: 0 }, data };
  }
}

async function fetchJsonSilent(path) {
  try {
    const response = await fetch(buildUrl(path));
    const data = await response.json();
    return { ok: response.ok, data };
  } catch {
    return { ok: false, data: { error: 'No se pudo consultar el detalle auxiliar' } };
  }
}

function renderFeaturedGame(game) {
  if (!game || !game.stats) return;

  featuredCoverEl.style.background = getCardGradient(game.id);
  featuredTitleEl.textContent = prettyGameName(game.nombre);
  featuredDescriptionEl.textContent = `ID ${game.id} · ${game.generos.join(', ')}`;
  featuredTagsEl.innerHTML = game.generos.map((genre) => `<span class="tag">${genre}</span>`).join('');
  featuredRatingEl.textContent = String(game.stats.rating);
  featuredHoursEl.textContent = `${game.stats.horas_juego} h`;
  featuredPriceEl.textContent = formatMoney(game.stats.precio);
}

function buildCompareReason(j1, j2, winnerName) {
  if (!j1 || !j2 || !j1.stats || !j2.stats) {
    return 'No fue posible calcular la explicación del ganador.';
  }

  if (j1.stats.rating !== j2.stats.rating) {
    const winner = j1.stats.rating > j2.stats.rating ? j1 : j2;
    const loser = winner === j1 ? j2 : j1;
    return `${prettyGameName(winnerName)} gana por mayor rating (${winner.stats.rating} vs ${loser.stats.rating}).`;
  }

  const winner = j1.stats.horas_juego >= j2.stats.horas_juego ? j1 : j2;
  const loser = winner === j1 ? j2 : j1;
  return `${prettyGameName(winnerName)} gana por desempate en horas jugadas (${winner.stats.horas_juego} vs ${loser.stats.horas_juego}) con rating igual (${j1.stats.rating}).`;
}

function renderGames(games) {
  state.shownGames = Array.isArray(games) ? games : [];

  if (state.shownGames.length === 0) {
    gamesGridEl.innerHTML = '<div class="empty">No hay juegos para mostrar con este filtro.</div>';
    libraryMetaEl.textContent = `0 resultados | Género activo: ${state.activeGenre}`;
    return;
  }

  gamesGridEl.innerHTML = state.shownGames
    .map((game) => {
      const genres = game.generos
        .map((genre) => `<span class="tag">${genre}</span>`)
        .join('');

      return `
        <article class="game-card">
          <div class="game-cover" style="background:${getCardGradient(game.id)}">
            <h4>${prettyGameName(game.nombre)}</h4>
          </div>
          <div class="game-meta">
            <div class="tags">${genres}</div>
            <div class="stats">
              <span>Rating: ${game.stats.rating}</span>
              <span>Horas: ${game.stats.horas_juego}</span>
            </div>
            <div class="price">${formatMoney(game.stats.precio)}</div>
            <div class="card-actions">
              <button class="btn detail-btn" data-identifier="${game.id}" type="button">Detalle</button>
              <button class="btn compare-select-btn" data-identifier="${game.id}" type="button">Comparar</button>
            </div>
          </div>
        </article>
      `;
    })
    .join('');

  libraryMetaEl.textContent = `${state.shownGames.length} resultados | Género activo: ${state.activeGenre}`;
}

function setActiveGenrePill(active) {
  document.querySelectorAll('.genre-pill').forEach((pill) => {
    const isActive = pill.dataset.genre === active;
    pill.classList.toggle('active', isActive);
  });
}

function renderGenres(genres) {
  genresListEl.innerHTML = genres
    .sort((a, b) => a.localeCompare(b))
    .map((genre) => `<button type="button" class="genre-pill" data-genre="${genre}">${genre}</button>`)
    .join('');

  setActiveGenrePill(state.activeGenre);
}

async function loadAllGames() {
  const { response, data } = await apiFetch('/juegos');
  if (response.ok && Array.isArray(data)) {
    state.allGames = data;
    renderGames(data);
    if (data.length > 0) {
      renderFeaturedGame(data[0]);
    }
  }
}

async function loadGenres() {
  const { response, data } = await apiFetch('/juegos/generos');
  if (response.ok && Array.isArray(data)) {
    renderGenres(data);
  }
}

async function initializeStore() {
  state.activeGenre = 'Todos';
  setActiveGenrePill('Todos');
  await Promise.all([loadAllGames(), loadGenres()]);
}

async function filterByGenre(genre) {
  state.activeGenre = genre;
  setActiveGenrePill(genre);

  if (genre === 'Todos') {
    renderGames(state.allGames);
    return;
  }

  const { response, data } = await apiFetch(`/juegos/generos/${encodeURIComponent(genre)}`);
  if (!response.ok || !Array.isArray(data)) return;

  const names = new Set(data);
  const filtered = state.allGames.filter((game) => names.has(game.nombre));
  renderGames(filtered);
}

document.getElementById('genre-all').addEventListener('click', async () => {
  await filterByGenre('Todos');
});

genresListEl.addEventListener('click', async (event) => {
  const button = event.target.closest('.genre-pill');
  if (!button) return;
  const genre = button.dataset.genre;
  await filterByGenre(genre);
});

document.getElementById('btn-refresh').addEventListener('click', async () => {
  await initializeStore();
  compareWinnerEl.textContent = 'Catálogo recargado.';
});

document.getElementById('form-filter').addEventListener('submit', async (event) => {
  event.preventDefault();
  const generos = commaListToArray(event.target.generos.value);
  const rating = event.target.rating.value.trim();
  const horas = event.target.horas.value.trim();
  const precio = event.target.precio.value.trim();

  if (!requireAtLeastOne([generos.length, rating, horas, precio])) {
    showResult(false, 'GET', '/juegos/', 400, {
      error: 'Debes ingresar al menos un filtro'
    });
    return;
  }

  const params = new URLSearchParams();
  generos.forEach((g) => params.append('genero', g));
  if (rating) params.set('rating', rating);
  if (horas) params.set('horas_juego', horas);
  if (precio) params.set('precio', precio);

  const path = `/juegos/?${params.toString()}`;
  const { response, data } = await apiFetch(path);
  if (response.ok && Array.isArray(data)) {
    state.activeGenre = generos.length > 0 ? generos.join(', ') : 'Filtro avanzado';
    setActiveGenrePill('');
    renderGames(data);
  }
});

document.getElementById('form-by-id').addEventListener('submit', async (event) => {
  event.preventDefault();
  const identifier = event.target.identifier.value.trim();
  const { response, data } = await apiFetch(`/juegos/${encodeURIComponent(identifier)}`);

  if (response.ok && data && data.id) {
    renderFeaturedGame(data);
    libraryMetaEl.textContent = `Detalle ampliado de ${prettyGameName(data.nombre)}`;
  }
});

document.getElementById('form-compare').addEventListener('submit', async (event) => {
  event.preventDefault();
  const id1 = event.target.id1.value.trim();
  const id2 = event.target.id2.value.trim();
  const { response, data } = await apiFetch(`/comparar/${encodeURIComponent(id1)}/${encodeURIComponent(id2)}`);

  if (response.ok && data.ganador) {
    const [game1Result, game2Result] = await Promise.all([
      fetchJsonSilent(`/juegos/${encodeURIComponent(id1)}`),
      fetchJsonSilent(`/juegos/${encodeURIComponent(id2)}`)
    ]);

    const reason = buildCompareReason(game1Result.data, game2Result.data, data.ganador);
    compareWinnerEl.innerHTML = `<strong>Ganador: ${prettyGameName(data.ganador)}</strong><br>${reason}`;

    const winnerGame = game1Result.data?.nombre === data.ganador
      ? game1Result.data
      : game2Result.data?.nombre === data.ganador
        ? game2Result.data
        : null;
    if (winnerGame) {
      renderFeaturedGame(winnerGame);
    }
  } else {
    compareWinnerEl.textContent = 'No fue posible comparar esos juegos.';
  }
});

gamesGridEl.addEventListener('click', async (event) => {
  const detailButton = event.target.closest('.detail-btn');
  if (detailButton) {
    const { response, data } = await apiFetch(`/juegos/${detailButton.dataset.identifier}`);
    if (response.ok) {
      renderFeaturedGame(data);
      libraryMetaEl.textContent = `Detalle ampliado de ${prettyGameName(data.nombre)}`;
    }
    return;
  }

  const compareButton = event.target.closest('.compare-select-btn');
  if (compareButton) {
    const compareForm = document.getElementById('form-compare');
    if (!compareForm.id1.value) {
      compareForm.id1.value = compareButton.dataset.identifier;
      compareWinnerEl.textContent = 'Juego 1 seleccionado. Elige juego 2.';
    } else {
      compareForm.id2.value = compareButton.dataset.identifier;
      compareWinnerEl.textContent = 'Juego 2 seleccionado. Presiona comparar.';
    }
  }
});

document.getElementById('form-add').addEventListener('submit', async (event) => {
  event.preventDefault();

  const body = {
    id: Number(event.target.id.value),
    nombre: event.target.nombre.value.trim(),
    generos: commaListToArray(event.target.generos.value),
    stats: {
      rating: Number(event.target.rating.value),
      horas_juego: Number(event.target.horas.value),
      precio: Number(event.target.precio.value)
    }
  };

  const { response } = await apiFetch('/juegos', {
    method: 'POST',
    body: JSON.stringify(body)
  }, true);

  if (response.ok) {
    event.target.reset();
    await initializeStore();
  }
});

document.getElementById('form-patch').addEventListener('submit', async (event) => {
  event.preventDefault();

  const identifier = event.target.identifier.value.trim();
  const rating = event.target.rating.value.trim();
  const horas = event.target.horas.value.trim();
  const precio = event.target.precio.value.trim();

  const body = {};
  if (rating) body.rating = Number(rating);
  if (horas) body.horas_juego = Number(horas);
  if (precio) body.precio = Number(precio);

  if (Object.keys(body).length === 0) {
    showResult(false, 'PATCH', `/juegos/${identifier}`, 400, {
      error: 'Debes enviar al menos un campo para modificar'
    });
    return;
  }

  const { response } = await apiFetch(`/juegos/${encodeURIComponent(identifier)}`, {
    method: 'PATCH',
    body: JSON.stringify(body)
  }, true);

  if (response.ok) {
    event.target.reset();
    await initializeStore();
  }
});

document.getElementById('form-delete').addEventListener('submit', async (event) => {
  event.preventDefault();

  const identifier = event.target.identifier.value.trim();
  const { response } = await apiFetch(`/juegos/${encodeURIComponent(identifier)}`, {
    method: 'DELETE'
  }, true);

  if (response.ok) {
    event.target.reset();
    await initializeStore();
  }
});

initializeStore();
