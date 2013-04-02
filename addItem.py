    def addItem(self):
        ''' Uses the addItem to create new content in an Org. '''
        portalId = self.__portalId__()

        #http://www.arcgis.com/apidocs/rest/index.html?additem.html
        #Example of existing - http://www.arcgis.com/sharing/rest/content/items/149a9bb14d604bd18f4597b21c19fac7/data
        #'text' : '{\"operationalLayers\": [],\"baseMap\": {\"title\": \"Light Gray Canvas NYC\",\"baseMapLayers\": [{\"visibility\": true,\"opacity\": 1,\"url\": \"http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer\"},{\"visibility\": true,\"opacity\": 1,\"isReference\": true,\"url\": \"http://tiles.arcgis.com/tiles/Fz6BBJUji5ArUSDM/arcgis/rest/services/Neighborhoods/MapServer\"}]},\"version\": \"1.7\"}',
        req = urllib2.Request( self.portalUrl + '/sharing/rest/content/users/'+self.username+'/addItem')                             
        # THIS IS JUST A SAMPLE.  YOU WILL NEED TO EDIT FOR YOUR SPECIFIC BASEMAP NEEDS
        req.add_data(urllib.urlencode({'token' : self.token,
                                       'f' : 'json',
                                       'text' : '{\"operationalLayers\": [],\"baseMap\": {\"title\": \"YourTitle\",\"baseMapLayers\": [\
                                       {\"visibility\": true,\"opacity\": 1,\"url\": \"http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer\"},\
                                       {\"visibility\": true,\"opacity\": 1,\"isReference\": true,\"url\": \"http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Reference/MapServer\"}]},\"version\": \"1.7\"}',
                                       'title' : 'Shaded Relief',
                                       'type' : 'Web Map',
                                       'tags' : 'basemap, Tallahassee, Leon County'}))

        return urllib2.urlopen(req)           
