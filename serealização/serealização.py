import xml.etree.ElementTree as ET

class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def to_xml_element(self):
        livro_element = ET.Element("livro")
        livro_element.set("id", str(self.id))

        titulo_element = ET.SubElement(livro_element, "titulo")
        titulo_element.text = self.titulo

        autor_element = ET.SubElement(livro_element, "autor")
        autor_element.text = self.autor

        return livro_element

class Livraria:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def to_xml(self):
        livraria_element = ET.Element("livraria")

        for livro in self.livros:
            livraria_element.append(livro.to_xml_element())

        return ET.tostring(livraria_element, encoding="unicode", method="xml")

    def salvar_xml(self, arquivo):
        tree = ET.ElementTree(ET.fromstring(self.to_xml()))
        tree.write(arquivo, encoding="utf-8", xml_declaration=True)

livro1 = Livro(1, "Python para Iniciantes", "João Silva")
livro2 = Livro(2, "Aprendendo Java", "Maria Souza")

livraria = Livraria()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

xml_string = livraria.to_xml()
print(xml_string)

livraria.salvar_xml("livraria.xml")