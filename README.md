# demo-failing-app

A tiny Python project that **fails CI on purpose**, used to test the
self-healing backend (Prpatch).

`src/utils.py` contains two intentional bugs (`average` and `is_even`), so
`pytest` fails. The failed CI run triggers `notify-on-failure.yml`, which calls
your backend. The AI agent should then open a PR fixing `src/utils.py`.

## Setup

1. Create a new GitHub repo (default branch must be `main`) and push this code.
2. Repo -> Settings -> Secrets and variables -> Actions -> add:
   - `WEBHOOK_URL`    = `https://<your-backend-or-ngrok-url>/webhook`
   - `WEBHOOK_SECRET` = same value as `WEBHOOK_SECRET` in the backend `.env`
3. Make sure the backend is running and `GITHUB_TOKEN` in its `.env` can write to this repo.
4. Push to `main`, or open/update a same-repository pull request. If CI fails, the notifier sends the failing commit to the backend. For PR failures, a repair PR targets that PR's source branch so you can merge the fix into the original PR. Fork PR failures are not forwarded.

## Run tests locally

    pip install -r requirements.txt
    python -m pytest -v
