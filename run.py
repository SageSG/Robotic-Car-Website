from webapp import app

# Enable running using python <filename> command in development mode
# Disable debug when submitting
if __name__ == '__main__':
    app.run(debug=True)