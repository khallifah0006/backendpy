from workout_recommendation import app, initialize_data

# Initialize data when the app starts
initialize_data()

if __name__ == "__main__":
    app.run()