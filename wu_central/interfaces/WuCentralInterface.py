import abc

class WuCentralInterface(abc.ABC):
    @abc.abstractmethod
    def openWhatsUp(self):
        pass

    @abc.abstractmethod
    def openWhatsUpAuto(self):
        pass
