from fastapi import Request
import time


async def time_request(request: Request, next):    
    start_time = time.time()
    
    response = await next(request)
    
    tempo_de_processo = time.time() - start_time
    
    response.headers['X-Process-Time'] = str(tempo_de_processo)

    return response