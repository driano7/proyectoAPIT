from CliUI import CliUI
if __name__=="__main__":
    ui=CliUI()
    try:
        ui.loop()
    except KeyboardInterrupt:
        print("Saliendo")
