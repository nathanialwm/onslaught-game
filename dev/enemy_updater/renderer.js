const FIELDS = [
  { key: 'name',            type: 'string', fullWidth: true },
  { key: 'level',           type: 'int' },
  { key: 'health',          type: 'int' },
  { key: 'attack',          type: 'int' },
  { key: 'attack_speed',    type: 'float', step: 0.1 },
  { key: 'defense',         type: 'int' },
  { key: 'accuracy',        type: 'int' },
  { key: 'dodge',           type: 'int' },
  { key: 'exp_reward',      type: 'int' },
  { key: 'gold_reward',     type: 'int' },
  { key: 'rarity_modifier', type: 'float', step: 0.001 }
];

let enemies = [];
let editingIndex = -1; // -1 = creating new enemy

const listEl = document.getElementById('enemy-list');
const editorEl = document.getElementById('editor');
const placeholderEl = document.getElementById('placeholder');
const titleEl = document.getElementById('editor-title');
const btnNew = document.getElementById('btn-new');
const btnSave = document.getElementById('btn-save');
const btnDelete = document.getElementById('btn-delete');
const statusMsg = document.getElementById('status-msg');
const btnDuplicate = document.getElementById('btn-duplicate');

// --- Build Form from FIELDS ---

function buildForm() {
  const formGrid = document.getElementById('form-grid');
  formGrid.innerHTML = '';
  for (const field of FIELDS) {
    const group = document.createElement('div');
    group.className = 'form-group' + (field.fullWidth ? ' full-width' : '');

    const label = document.createElement('label');
    label.setAttribute('for', 'field-' + field.key);
    label.textContent = field.key.replace(/_/g, ' ');
    group.appendChild(label);

    const input = document.createElement('input');
    input.id = 'field-' + field.key;
    input.type = field.type === 'string' ? 'text' : 'number';
    if (field.type !== 'string') input.min = '0';
    if (field.step) input.step = field.step;
    group.appendChild(input);

    formGrid.appendChild(group);
  }
}

// --- Load & Render List ---

async function loadEnemies() {
  enemies = await window.enemyAPI.loadEnemies();
  renderList();
}

function renderList() {
  listEl.innerHTML = '';
  enemies.forEach((enemy, index) => {
    const item = document.createElement('div');
    item.className = 'enemy-list-item' + (index === editingIndex ? ' active' : '');
    item.textContent = enemy.id + '. ' + enemy.name;
    item.addEventListener('click', () => selectEnemy(index));
    listEl.appendChild(item);
  });
}

// --- Select / New ---

function selectEnemy(index) {
  editingIndex = index;
  const enemy = enemies[index];

  FIELDS.forEach(({ key }) => {
    document.getElementById('field-' + key).value = enemy[key] ?? '';
  });

  titleEl.textContent = 'Edit: ' + enemy.name;
  btnDelete.classList.remove('hidden');
  showEditor();
  renderList();
}

function newEnemy() {
  editingIndex = -1;

  FIELDS.forEach(({ key, type }) => {
    const input = document.getElementById('field-' + key);
    input.value = type === 'string' ? '' : '';
  });

  titleEl.textContent = 'New Enemy';
  btnDelete.classList.add('hidden');
  showEditor();
  renderList();
}

function showEditor() {
  placeholderEl.style.display = 'none';
  editorEl.style.display = 'block';
  statusMsg.textContent = '';
}

// --- Save ---

async function save() {
  const enemy = {};
  for (const { key, type } of FIELDS) {
    const raw = document.getElementById('field-' + key).value.trim();
    if (raw === '') {
      showStatus('Please fill in all fields.', true);
      return;
    }
    if (type === 'int') enemy[key] = parseInt(raw, 10);
    else if (type === 'float') enemy[key] = parseFloat(raw);
    else enemy[key] = raw;
  }

  if (editingIndex === -1) {
    const maxId = enemies.reduce((max, e) => Math.max(max, e.id || 0), 0);
    enemy.id = maxId + 1;
    enemies.push(enemy);
    editingIndex = enemies.length - 1;
  } else {
    enemy.id = enemies[editingIndex].id;
    enemies[editingIndex] = enemy;
  }

  await window.enemyAPI.saveEnemies(enemies);
  titleEl.textContent = 'Edit: ' + enemy.name;
  btnDelete.classList.remove('hidden');
  renderList();
  showStatus('Saved successfully.');
}

// --- Delete ---

async function deleteEnemy() {
  if (editingIndex === -1) return;

  const name = enemies[editingIndex].name;
  if (!confirm('Delete "' + name + '"?')) return;

  enemies.splice(editingIndex, 1);
  await window.enemyAPI.saveEnemies(enemies);

  editingIndex = -1;
  editorEl.style.display = 'none';
  placeholderEl.style.display = 'flex';
  renderList();
  showStatus('Deleted "' + name + '".');
}

// --- Open New Window ---
function openNewWindow() {
  window.enemyAPI.openNewWindow();
}

// --- Status ---

function showStatus(msg, isError) {
  statusMsg.textContent = msg;
  statusMsg.style.color = isError ? '#f38ba8' : '#a6e3a1';
}

// --- Events ---

btnDuplicate.addEventListener('click', openNewWindow);
btnNew.addEventListener('click', newEnemy);
btnSave.addEventListener('click', save);
btnDelete.addEventListener('click', deleteEnemy);

buildForm();
loadEnemies();
