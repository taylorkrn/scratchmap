from scratchmap import create_app, db

#Run create_app() Method in __init__.py in folder scratchmap
app = create_app()

if __name__ == '__main__':
    #Debug allows website to be continuously updated as the code is being updated
    app.run(debug=True)
