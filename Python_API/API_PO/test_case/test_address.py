from MyPythonTest.Python_API.API_PO.api_page.address_page import AddressPage


class TestAddressPage:
    def setup_class(self):
        self.address_page = AddressPage()

    def test_get(self):
        member_message = self.address_page.get_member_info()
        assert member_message['errcode'] in [0, 60111]

    def test_add(self):
        member_message = self.address_page.add_member()
        assert member_message['errcode'] in [0, 60104]

    def test_delete(self):
        member_message = self.address_page.delete_member()
        assert member_message['errcode'] in [0, 60111]

    def test_update(self):
        member_message = self.address_page.update_member()
        assert member_message['errcode'] in [0, 60111]