def export_to_orientdb(self, batch_size, db_url, user_name, password, root_password,vertexTypeColumnName=None, edgeTypeColumnName=None):
    self._scala.exportToOrientdb(batch_size, db_url, user_name, password, root_password,self._tc._jutils.convert.to_scala_option(vertexTypeColumnName),self._tc._jutils.convert.to_scala_option(edgeTypeColumnName))