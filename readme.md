# CLI Bookmarks
##### By Erika Sanchez

### Installation
1. Fork and clone this repository
2. In the directory for this repo, in your commande line, use: `pipenv install`
3. Then, use: `psql`
4. Then, use: `CREATE DATABASE bookmarks;`
5. Then, use: `\c bookmarks`
6. In a new CLI tab/window, use: `pipenv shell`
7. Lastly, use: `python main.py`

To exit the shell, use: `exit`

### Use 
- You will be asked "What would you like to do?" Simply enter the number of the option you'd wish to perform.

- From there, the rest of the prompt will guide you the rest of the way. 

- In the CLI window where you've activated the Postgres Database, you can type `SELECT * FROM bookmark` to see all of the bookmarks that have been added. 