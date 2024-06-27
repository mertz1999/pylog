from pylog.log import Log


logger = Log(save=True)


logger.info('Hi this is a test')
logger.warning('Hi this is a test')
logger.error('Hi this is a test')