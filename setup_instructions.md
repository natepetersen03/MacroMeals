Set-up instructions:

1) install conda and run "conda env create -f environment.yml" in the command line to download all of the necessary dependencies. Then, activate the environment.
2) create a database called "macro_meals" with a table "recipes" using "final_dataset.csv" and SQL's table data import wizard. Make "name" the primary key and if it errors, make its type VARCHAR(50)
3) go to backend.py and edit username/password, the server (if necessary), and the socket to reflect your local mysql configuration.
4) cd into macromeals-frontend and run "npm run start:both". This should start the backend on localhost port 5000 and the frontend on localhost port 3000.