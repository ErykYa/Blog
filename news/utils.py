class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()


class Mixin2(object):
    mixin_prop = ''

    def umnozh(self, s):
        return s * 2
