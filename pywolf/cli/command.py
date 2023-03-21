import asyncio

async def run(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd
        , stdout=asyncio.subprocess.PIPE
        , stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate()
    
    if stdout:
        return stdout.decode()
    
    if stderr:
        return stderr.decode()
    
async def echo(cmd):
    resp = await run(cmd)
    print(resp)

if __name__=='__main__':
    asyncio.run(echo('ls -alh'))