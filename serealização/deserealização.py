import xml.etree.ElementTree as ET

class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    @classmethod
    def from_xml_element(cls, element):
        id = element.get("id")
        titulo = element.find("titulo").text
        autor = element.find("autor").text
        return cls(id, titulo, autor)

    def __repr__(self):
        return f"Livro(id={self.id}, titulo={self.titulo}, autor={self.autor})"


class Livraria:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    @classmethod
    def from_xml(cls, xml_data):
        root = ET.fromstring(xml_data)
        return cls._parse_root(root)

    @classmethod
    def from_xml_file(cls, arquivo):
        tree = ET.parse(arquivo)
        root = tree.getroot()
        return cls._parse_root(root)

    @classmethod
    def _parse_root(cls, root):
        livraria = cls()
        for livro_element in root.findall("livro"):
            livro = Livro.from_xml_element(livro_element)
            livraria.adicionar_livro(livro)
        return livraria

    def __repr__(self):
        return f"Livraria(livros={self.livros})"

xml_arquivo = "livraria.xml"

livraria = Livraria.from_xml_file(xml_arquivo)

print(livraria)