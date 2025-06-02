from MTG_Model import Model
from MTG_Controller import Controller
from MTG_View import View

def main():
    model = Model()
    controller = Controller(model)
    view = View(controller)

if __name__ == '__main__':
    main()
