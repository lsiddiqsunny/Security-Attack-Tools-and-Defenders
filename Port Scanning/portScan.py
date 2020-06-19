def Curl(host):
    """
    Returns True if host responds to a curl request
    """
    import subprocess, platform

    args = "curl "+ host
    need_sh = False if  platform.system().lower()=="windows" else True

    return subprocess.call(args, shell=need_sh) == 0

for i in range(1,65536):
    print(Curl("192.168.0.104:"+str(i)))