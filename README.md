# Late Show API

The Late Show API is a Flask-based RESTful API designed to manage episodes, guests, and appearances of the Late Show. It offers endpoints for retrieving episodes, getting details of a specific episode, retrieving guests, and managing appearances.

### Table of Contents
1. [Introduction](#introduction)
2. [Technology Used](#technology-used)
3. [Models](#models)
4. [Routes](#routes)
5. [Setup Instructions](#setup-instructions)
6. [Usage](#usage)
7. [Contribution](#contribution)
8. [License](#license)
9. [Author](#author)

## Introduction

The Late Show API provides data about episodes, guests, and appearances on the Late Show. It allows users to retrieve information about episodes, guests, and appearances, as well as create and delete appearances.

## Technology Used

- **Flask**: Flask is a micro web framework written in Python. It is used to create the RESTful API endpoints and handle HTTP requests and responses.
- **SQLAlchemy**: SQLAlchemy is an SQL toolkit and Object-Relational Mapping (ORM) library for Python. It is used for database operations and to define the database models.
- **SQLite**: SQLite is a lightweight, serverless, and self-contained SQL database engine. It is used as the database management system for storing and querying Late Show data in this project.
- **Python**: Python is a high-level programming language known for its simplicity and readability. It is used to write the backend logic of the Late Show API.

## Models

The API implements the following data model:

- **Episode**: Represents an episode of the Late Show with attributes `id`, `title`, and `air_date`.
- **Guest**: Represents a guest on the Late Show with attributes `id`, `name`, and `occupation`.
- **Appearance**: Represents the appearance of a guest on an episode with attributes `id`, `episode_id`, `guest_id`, and `rating`.

## Routes

The API provides the following routes with corresponding HTTP methods:

- **GET /episodes**: Retrieve a list of all episodes.
- **GET /episodes/:episode_id**: Retrieve details of a specific episode by ID.
- **GET /guests**: Retrieve a list of all guests.
- **POST /appearances**: Create a new appearance of a guest on an episode.
- **DELETE /appearances/:appearance_id**: Delete an appearance by ID.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Moringa-SDF-PTO5/LateShow-Josephine-Nzioka
   cd Lateshow-Josephine-Nzioka
