install:
	python -m venv .venv && ./.venv/bin/pip install -r requirements.txt

run:
	./.venv/bin/streamlit run streamlit_app.py

zip:
	python bundle.py
