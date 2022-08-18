from configparser import ConfigParser


def conf_reader(section,element):
    conf = ConfigParser()
    conf.read('../ConfigData/config.ini')
    return conf.get(section,element)


