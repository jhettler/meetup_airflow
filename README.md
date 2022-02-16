# Airflow meetup

## Prerequisities
* Docker
* MacOS/Linux, I haven't tested it under Windows
* VS Code

## Running standalone Airflow
For development and testing purpose
1. `git clone https://github.com/jhettler/meetup_airflow.git`
2. Open in container in VS Code. Plugin `Remote - Containers` and run command `Remote - Containers: Open Folder In Container`
3. Everything should be set up in devcontainer.
4. Open terminal in container and run `airflow standalone`
5. Grab a generated admin password from terminal
6. Airflow should run with example DAGS on port 8080
7. (Optional) VS Code should open the port 8080 from container, if not, you have to open it manually in `devcontainer.json`