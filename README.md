# BudgetMe

BudgetMe is a personal finance application that helps users analyze their spending, create budgets, and save more money. It connects to Spendee or imports transactions by other means to provide a comprehensive view of the user's financial situation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7+
- Node.js and npm
- Vue.js

### Installing

1. Clone the repository
```
git clone https://github.com/ionabio/BudgetMe.git
```

2. Make a python environment

```
python3 -m venv budgetme
.\budgetme\Scripts\activate
```

3. Install Python dependencies
```
cd BudgetMe
pip3 install -r requirements.txt
```

4. Install JavaScript dependencies
```
cd frontend
npm install
```

### Running the Application

1. Start the backend server
```
cd backend
python app.py
```

2. In a new terminal window, start the frontend server
```
cd frontend
npm run serve
```

The application should now be running at `http://localhost:8080`.

## Project Structure

The project has two main parts: the backend and the frontend.

The backend is a Flask application that connects to Spendee, analyzes spending, and creates budgets. It is written in Python and uses libraries like Selenium, NumPy, and Pandas.

The frontend is a Vue.js application that displays the data from the backend in a user-friendly way. It is written in JavaScript and uses the Vue.js framework.

## Built With

- [Flask](http://flask.pocoo.org/) - The web framework used for the backend
- [Vue.js](https://vuejs.org/) - The framework used for the frontend
- [Selenium](https://www.selenium.dev/) - Used to automate web browser interaction
- [NumPy](https://numpy.org/) - Used for numerical computation
- [Pandas](https://pandas.pydata.org/) - Used for data manipulation and analysis

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Your Name** - *Initial work* - [ionabio](https://github.com/ionabio)

See also the list of [contributors](https://github.com/ionabio/BudgetMe/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc