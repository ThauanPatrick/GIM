from xml.dom.minidom import parse

arquivo_xml = parse('C:/Users/thauan.estagiario/Desktop/New_Python/ex.tif.xml')

my_node_list = arquivo_xml.getElementsByTagName("SyncDate")

my_n_node = my_node_list[0]
my_child = my_n_node.firstChild
my_text = my_child.data

print my_text


