# Transpontual Frontend Dashboard

Dashboard web em Flask para o sistema de gestão de frotas da Transpontual.

## Tecnologias
- Flask
- Jinja2 Templates
- Bootstrap/Tailwind CSS
- JavaScript

## Configuração
O frontend se conecta ao backend via variável `API_BASE`:
- Produção: `https://web-production-256fe.up.railway.app`
- Local: `http://localhost:8000`

## Deploy
Este repositório é automaticamente deployado no Railway como frontend dashboard.

## Páginas
- `/` - Dashboard principal
- `/login` - Página de login
- `/vehicles` - Gestão de veículos
- `/drivers` - Gestão de motoristas
- `/checklists` - Checklists dos veículos

## Desenvolvimento Local
```bash
pip install -r requirements.txt
python run.py
```
