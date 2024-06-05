class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, element_id):
        if not self.root:
            return None
        return self._get_element_by_id_recursive(self.root, element_id)

    def _get_element_by_id_recursive(self, node, element_id):
        if node['id'] == element_id:
            return node
        for child in node.get('children', []):
            result = self._get_element_by_id_recursive(child, element_id)
            if result:
                return result
        return None

    pass
