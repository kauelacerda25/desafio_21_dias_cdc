# Flask TODO List

English / Português

---

**Project Overview (English)**

A small Flask TODO list application using SQLite via Flask-SQLAlchemy. The app provides basic CRUD operations (create, read, update, delete) for tasks, a responsive dark-mode UI, accessible controls and lightweight client-side edits for a smoother user experience.

**Features**
- Create tasks
- List tasks
- Update tasks (inline edit form)
- Delete tasks
- Simple dark-mode UI with animations (CSS)
- Accessibility improvements (aria attributes)

**Requirements**
- Python 3.8+
- Virtual environment recommended
- Packages: `Flask`, `Flask-SQLAlchemy`

**Quick Setup (Windows PowerShell)**

1. Create and activate a virtual environment (if not already):

```powershell
python -m venv .\venv
.\venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install directly:

```powershell
pip install Flask Flask_SQLAlchemy
```

**Run the app**

From the project folder:

```powershell
python app.py
```

Open your browser at `http://127.0.0.1:5000/`.

**Routes**
- `GET /` — render the task list page
- `POST /create` — create a new task (form field `description`)
- `POST /update/<id>` — update task with id (form field `description`)
- `POST /delete/<id>` — delete task with id

**Notes**
- The app uses SQLite by default at `sqlite:///site.db` (file created in the project folder).
- The `Task.description` model field is marked `unique=True` — duplicate descriptions will be rejected.
- The HTML includes a small client-side script to toggle inline edit forms; if you prefer full AJAX behavior I can add fetch-based endpoints.

**Troubleshooting**
- If the app fails to run, ensure your virtualenv is active and required packages are installed.
- If port 5000 is in use, stop the other process or change `app.run(debug=True, port=XXXX)` in `app.py`.
- Database errors: remove `site.db` only if you understand the data will be lost; you can also inspect with a SQLite viewer.

---

**Visão Geral (Português)**

Uma pequena aplicação Flask de lista de tarefas usando SQLite via Flask-SQLAlchemy. A aplicação oferece operações CRUD básicas (criar, listar, editar, excluir) para tarefas, com UI dark-mode responsiva, melhorias de acessibilidade e edição inline para melhor experiência do usuário.

**Recursos**
- Criar tarefas
- Listar tarefas
- Editar tarefas (formulário inline)
- Excluir tarefas
- UI em modo escuro com animações (CSS)
- Melhorias de acessibilidade (atributos aria)

**Requisitos**
- Python 3.8+
- Recomenda-se usar um ambiente virtual
- Pacotes: `Flask`, `Flask-SQLAlchemy`

**Instalação Rápida (Windows PowerShell)**

1. Criar e ativar ambiente virtual:

```powershell
python -m venv .\venv
.\venv\Scripts\activate
```

2. Instalar dependências:

```powershell
pip install -r requirements.txt
```

Se não existir `requirements.txt`, instale diretamente:

```powershell
pip install Flask Flask_SQLAlchemy
```

**Executar a aplicação**

Na pasta do projeto:

```powershell
python app.py
```

Abra o navegador em `http://127.0.0.1:5000/`.

**Rotas**
- `GET /` — renderiza a página com a lista de tarefas
- `POST /create` — criar nova tarefa (campo do formulário `description`)
- `POST /update/<id>` — atualizar tarefa com id (campo do formulário `description`)
- `POST /delete/<id>` — deletar tarefa com id

**Observações**
- O app usa SQLite por padrão em `sqlite:///site.db` (arquivo criado na pasta do projeto).
- O campo `Task.description` é `unique=True` — descrições duplicadas serão rejeitadas.
- O HTML contém um script simples para alternar o formulário de edição inline; se preferir comportamento AJAX eu posso implementar.

**Solução de Problemas**
- Se a aplicação não iniciar, verifique se o ambiente virtual está ativo e se os pacotes necessários estão instalados.
- Se a porta 5000 estiver em uso, mate o processo ou altere `app.run(debug=True, port=XXXX)` em `app.py`.
- Erros de banco: remova `site.db` apenas se souber que os dados serão perdidos; também é possível inspecionar com um visualizador SQLite.

---

If you want, I can also:
- Add a `requirements.txt` file with pinned versions.
- Add a small `Makefile` or PowerShell script to automate setup.
- Implement AJAX-based updates for smoother UX.

Se quiser, posso também:
- Adicionar `requirements.txt` com versões fixas.
- Criar um script PowerShell para automatizar setup/execução.
- Implementar atualizações via AJAX para UX sem recarga de página.
