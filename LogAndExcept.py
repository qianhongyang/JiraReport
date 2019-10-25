import functools
import logging

# 常规错误日志异常处理
def except_decorate(content=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception:
                logger().error(":%s" %(content))
                exit(1)
        return wrapper

    return decorator
#日志控制
def logger():

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - '
                               '%(levelname)s: %(message)s')
    loggerl = logging.getLogger(__name__)

    return loggerl