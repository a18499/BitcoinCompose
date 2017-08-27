
import uuid

print "Insert how many node you want to create"
numberOfDockerNode = input()
print "Create "+str(numberOfDockerNode)+" node"
with open("docker-compose.yml", "a") as myfile:
    i=0
    while i < numberOfDockerNode:
        portsNumber = 20001+i
        nodeName = uuid.uuid4()
        print "Node Name: "+str(nodeName)
        myfile.write(" "+str(nodeName)+":")
        myfile.write("\n")
        myfile.write("  image: bitcoinnode")
        myfile.write("\n")
        myfile.write("  ports:")
        myfile.write("\n")
        myfile.write("   - "+str(portsNumber)+":18332")
        myfile.write("\n")
        myfile.write("  depends_on:")
        myfile.write("\n")
        myfile.write("   - a")
        myfile.write("\n")
        myfile.write("  links:")
        myfile.write("\n")
        myfile.write("   - a")
        myfile.write("\n")
        i+=1
print "Create Done "