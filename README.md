# Football-Management-System-with-Captcha-Security-Integration

## Overview
The Football Management System is a robust desktop application designed to manage football teams, players, and matches. It is built using **Python (Tkinter)** for the user interface, **MySQL** for data storage, and **Flask** with **Google reCAPTCHA** for enhanced security. The system includes features such as team and player management, match tracking, player search, and team ranking based on accumulated points.

This system aims to provide an intuitive experience for users while ensuring data integrity and security, making it a perfect tool for managing football leagues and competitions.

## Features

- **User Authentication**: Integration of **Google reCAPTCHA** using **Flask** ensures that only human users can access the application, preventing unauthorized bot access.
- **Team Management**: Admin can add, update, and delete football teams. Each team is limited to 11 players, enforced by **MySQL triggers**.
- **Player Management**: Admin can add and update player records, with efficient search by **ID or player name** for quick retrieval.
- **Match Management**: Users can enter match details, and the system tracks team rankings based on accumulated points.
- **Data Integrity**: **MySQL triggers** enforce rules like team player limits, ensuring no more than 11 players are assigned to each team.
- **Search Functionality**: Provides user-friendly search options for retrieving player information quickly.
- **Web-Desktop Integration**: The system combines desktop functionality with web-based authentication through **Flask**, creating a seamless experience.

## Technologies Used
- **Python**: Tkinter for the GUI-based desktop application
- **MySQL**: Backend database for storing and managing team, player, and match data
- **Flask**: Web framework to handle Google reCAPTCHA integration
- **Google reCAPTCHA**: To secure the login page and prevent bot access
- **SQL Triggers**: To enforce data integrity by limiting team sizes

## Installation

### Prerequisites:
1. **Python** 3.x
2. **MySQL** database server
3. **Flask** and **MySQL connector** libraries

### Steps to Run:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/football-management-system.git
    cd football-management-system
    ```

2. **Set up the MySQL Database:**
    - Create a MySQL database and import the schema from `database_schema.sql`.

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    - For web authentication:
    ```bash
    python app.py
    ```

5. **Launch the GUI**: Run the Tkinter-based desktop application and interact with the system.

## Usage

1. Upon running the application, users will be required to complete a Google reCAPTCHA verification to access the system.
2. Admin can add or modify football team details and player records.
3. The system provides search options to quickly retrieve player details by name or ID.
4. Match details can be added, and team rankings will automatically update based on match points.

## Future Improvements

- **Live Leaderboards**: Integration of live leaderboards based on ongoing match results.
- **Match Statistics**: Addition of detailed match statistics for deeper insights.
- **Mobile App Integration**: Extending the application to mobile platforms for better access.

## Output

![image](https://github.com/user-attachments/assets/c5790f66-8de5-4b9f-8987-fbeb4d3fd220)

![image](https://github.com/user-attachments/assets/90992c05-a349-44b5-9cdd-a4f2ee65fa13)

![WhatsApp Image 2025-04-29 at 8 45 23 PM](https://github.com/user-attachments/assets/39cf769a-d935-421e-a0a8-bf1716a47db0)

![image](https://github.com/user-attachments/assets/76db2aa0-8a98-4e2a-83eb-e2fb625b1672)

![image](https://github.com/user-attachments/assets/43548a2d-84ba-4753-940a-a258601ec5ff)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: If you have any issues or questions, feel free to open an issue or pull request.
