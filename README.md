# Namma GPT

Namma GPT is a lightweight, containerized chatbot API built with Python and Flask, packaged with Docker, and delivers Bangalore-inspired responses with a casual, local touch. It’s a minimal project designed for fun experimentation, using a simple rule-based system to keep interactions fast, fun, and engaging.

## Overview
- **Purpose:** A simple chatbot that delivers informal, location-inspired responses.
- **Tech Stack:** Python, Flask, Docker.
- **Features:** Basic API endpoint for text input and JSON responses.

## How to Run
1. **Clone the Repository:**
   ```bash
   git clone (https://github.com/slothrulez/Namma-GPT)
   cd namma-gpt
   ```
2. Build the Docker Image:   
   ```bash
   docker build -t namma-gpt .
   ```

3. Run the Container:
   ```bash
   docker run -p 5000:5000 namma-gpt
   ```

4. Test the API:
   * Send a POST request:
   ```bash
   curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "hi"}'
   ```
   * Example response: {"response": "Hey there, welcome to Bangalore!"}

## Project Structure

  * app.py: Core Flask application and API logic.
  * responses.py: Contains the chatbot’s response logic and phrases.
  * Dockerfile: Configuration for containerizing the app.
  * requirements.txt: Lists Python dependencies.
    
## Future Improvements
  * Add CORS support for the web interface.
  * Deploy to a cloud platform like Heroku or AWS.
  * Expand the response library with more phrases.

## Author
Created by [slothrulez](https://github.com/slothrulez). Feel free to contribute!    
   
