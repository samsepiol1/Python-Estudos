from optparse import OptionParser
from socket import*
import json
def h2ip(host):
    try:
        ip=gethostbyname(host)
        return ip
    except:
        return None
host_name='www.google.com'
print(h2ip(host_name))
def connecto(host, port):
    try:
        s=socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        return s
    except:
        s.close()
        return None
host_name='www.google.com'
port=80
resultado=connecto(host_name,port)
print(resultado)
def bgrabber(sock):
    try:
        sock.send("Scann...\r\n")
        banner=sock.recv(1024)
        return banner
    except:
        return None
def scan(host,port):
    sock=connecto(host,port)
    setdefaulttimeout(5)
    if sock:
        print("[+] Conectando com %s:%d")
        banner=bgrabber(sock)
        if banner:
            print("[+] Banner: %s" %banner)
        else:
            print("Não foi possível executar o alvo")
            sock.close()
    else:
        print("Não foi possível conectar com {}:{}".format(host,port))
if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-a", "--alvo", dest="host", type="string",
                      help="Insira o nome do host alvo", metavar="exemplo.com")
    parser.add_option("-p", "--porta", dest="portas", type="string",
                      help="Portas que deseja scanear separadas por virgulas", metavar="PORT")

    (options, args) = parser.parse_args()

    if options.host == None or options.ports == None:
        parser.print_help()
    else:
        host = options.host
        ports = (options.ports).split(",")
        try:
            ports = list(filter(int, ports))  # Armazena as portas numa lista.
            ip = h2ip(host)  # Nome do Domínio IP.
            if ip:
                print("[+] Executando Scanner: %s" % host)
                print("[+] Alvo IP: %s" % ip)
                for port in ports:
                    scan(host, int(port))
            else:
                print("[!] Host Inválido !!")
        except:
            print("[!] Lista de portas inválidas (ex: -p 21,22,53,..)")

host_name2='www.academia.edu'
port=80,50,443
resultado3=scan(host_name2,port)
