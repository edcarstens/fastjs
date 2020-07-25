class Opov(object):
    negMethod = 'ov_neg'
    posMethod = 'ov_pos'
    absMethod = 'ov_abs'
    invertMethod = 'ov_invert'
    complexMethod = 'ov_complex'
    intMethod = 'ov_int'
    longMethod = 'ov_long'
    floatMethod = 'ov_float'
    octMethod = 'ov_oct'
    hexMethod = 'ov_hex'
    indexMethod = 'ov_index'
    lenMethod = 'ov_len'
    addMethod = 'ov_add'
    subMethod = 'ov_sub'
    mulMethod = 'ov_mul'
    floordivMethod = 'ov_floordiv'
    modMethod = 'ov_mod'
    divmodMethod = 'ov_divmod'
    lshiftMethod = 'ov_lshift'
    rshiftMethod = 'ov_rshift'
    andMethod = 'ov_and'
    xorMethod = 'ov_xor'
    orMethod = 'ov_or'
    divMethod = 'ov_div'
    truedivMethod = 'ov_truediv'
    raddMethod = 'ov_radd'
    rsubMethod = 'ov_rsub'
    rmulMethod = 'ov_rmul'
    rdivMethod = 'ov_rdiv'
    rtruedivMethod = 'ov_rtruediv'
    rfloordivMethod = 'ov_rfloordiv'
    rmodMethod = 'ov_rmod'
    rdivmodMethod = 'ov_rdivmod'
    rpowMethod = 'ov_rpow'
    rlshiftMethod = 'ov_rlshift'
    rrshiftMethod = 'ov_rrshift'
    randMethod = 'ov_rand'
    rxorMethod = 'ov_rxor'
    rorMethod = 'ov_ror'
    iaddMethod = 'ov_iadd'
    isubMethod = 'ov_isub'
    imulMethod = 'ov_imul'
    idivMethod = 'ov_idiv'
    itruedivMethod = 'ov_itruediv'
    ifloordivMethod = 'ov_ifloordiv'
    imodMethod = 'ov_imod'
    ilshiftMethod = 'ov_ilshift'
    irshiftMethod = 'ov_irshift'
    iandMethod = 'ov_iand'
    ixorMethod = 'ov_ixor'
    iorMethod = 'ov_ior'
    ltMethod = 'ov_lt'
    leMethod = 'ov_le'
    eqMethod = 'ov_eq'
    neMethod = 'ov_ne'
    gtMethod = 'ov_gt'
    geMethod = 'ov_ge'
    getitemMethod = 'ov_getitem'
    delitemMethod = 'ov_delitem'
    powMethod = 'ov_pow'
    ipowMethod = 'ov_ipow'
    callMethod = 'ov_call'
    def __init__(self, x=''):
        self.x = x if x else 'x'  # expression string
    def __str__(self):
        return self.x
    def _mcall1(self, m):
        return self.x + '.' + m + '()'
    def _mcall2(self, m, x):
        return self.x + '.' + m + '(' + str(x) + ')'
    def __neg__(self):
        return Opov(self._mcall1(self.negMethod))
    def __pos__(self):
        return Opov(self._mcall1(self.posMethod))
    def __abs__(self):
        return Opov(self._mcall1(self.absMethod))
    def __invert__(self):
        return Opov(self._mcall1(self.invertMethod))
    def __complex__(self):
        return Opov(self._mcall1(self.complexMethod))
    def __int__(self):
        return Opov(self._mcall1(self.intMethod))
    def __long__(self):
        return Opov(self._mcall1(self.longMethod))
    def __float__(self):
        return Opov(self._mcall1(self.floatMethod))
    def __oct__(self):
        return Opov(self._mcall1(self.octMethod))
    def __hex__(self):
        return Opov(self._mcall1(self.hexMethod))
    def __index__(self):
        return Opov(self._mcall1(self.indexMethod))
    def __len__(self):
        return Opov(self._mcall1(self.lenMethod))
    def __add__(self, x):
        return Opov(self._mcall2(self.addMethod, x))
    def __sub__(self, x):
        return Opov(self._mcall2(self.subMethod, x))
    def __mul__(self, x):
        return Opov(self._mcall2(self.mulMethod, x))
    def __floordiv__(self, x):
        return Opov(self._mcall2(self.floordivMethod, x))
    def __mod__(self, x):
        return Opov(self._mcall2(self.modMethod, x))
    def __divmod__(self, x):
        return Opov(self._mcall2(self.divmodMethod, x))
    def __lshift__(self, x):
        return Opov(self._mcall2(self.lshiftMethod, x))
    def __rshift__(self, x):
        return Opov(self._mcall2(self.rshiftMethod, x))
    def __and__(self, x):
        return Opov(self._mcall2(self.andMethod, x))
    def __xor__(self, x):
        return Opov(self._mcall2(self.xorMethod, x))
    def __or__(self, x):
        return Opov(self._mcall2(self.orMethod, x))
    def __div__(self, x):
        return Opov(self._mcall2(self.divMethod, x))
    def __truediv__(self, x):
        return Opov(self._mcall2(self.truedivMethod, x))
    def __radd__(self, x):
        return Opov(self._mcall2(self.raddMethod, x))
    def __rsub__(self, x):
        return Opov(self._mcall2(self.rsubMethod, x))
    def __rmul__(self, x):
        return Opov(self._mcall2(self.rmulMethod, x))
    def __rdiv__(self, x):
        return Opov(self._mcall2(self.rdivMethod, x))
    def __rtruediv__(self, x):
        return Opov(self._mcall2(self.rtruedivMethod, x))
    def __rfloordiv__(self, x):
        return Opov(self._mcall2(self.rfloordivMethod, x))
    def __rmod__(self, x):
        return Opov(self._mcall2(self.rmodMethod, x))
    def __rdivmod__(self, x):
        return Opov(self._mcall2(self.rdivmodMethod, x))
    def __rpow__(self, x):
        return Opov(self._mcall2(self.rpowMethod, x))
    def __rlshift__(self, x):
        return Opov(self._mcall2(self.rlshiftMethod, x))
    def __rrshift__(self, x):
        return Opov(self._mcall2(self.rrshiftMethod, x))
    def __rand__(self, x):
        return Opov(self._mcall2(self.randMethod, x))
    def __rxor__(self, x):
        return Opov(self._mcall2(self.rxorMethod, x))
    def __ror__(self, x):
        return Opov(self._mcall2(self.rorMethod, x))
    def __iadd__(self, x):
        return Opov(self._mcall2(self.iaddMethod, x))
    def __isub__(self, x):
        return Opov(self._mcall2(self.isubMethod, x))
    def __imul__(self, x):
        return Opov(self._mcall2(self.imulMethod, x))
    def __idiv__(self, x):
        return Opov(self._mcall2(self.idivMethod, x))
    def __itruediv__(self, x):
        return Opov(self._mcall2(self.itruedivMethod, x))
    def __ifloordiv__(self, x):
        return Opov(self._mcall2(self.ifloordivMethod, x))
    def __imod__(self, x):
        return Opov(self._mcall2(self.imodMethod, x))
    def __ilshift__(self, x):
        return Opov(self._mcall2(self.ilshiftMethod, x))
    def __irshift__(self, x):
        return Opov(self._mcall2(self.irshiftMethod, x))
    def __iand__(self, x):
        return Opov(self._mcall2(self.iandMethod, x))
    def __ixor__(self, x):
        return Opov(self._mcall2(self.ixorMethod, x))
    def __ior__(self, x):
        return Opov(self._mcall2(self.iorMethod, x))
    def __lt__(self, x):
        return Opov(self._mcall2(self.ltMethod, x))
    def __le__(self, x):
        return Opov(self._mcall2(self.leMethod, x))
    def __eq__(self, x):
        return Opov(self._mcall2(self.eqMethod, x))
    def __ne__(self, x):
        return Opov(self._mcall2(self.neMethod, x))
    def __gt__(self, x):
        return Opov(self._mcall2(self.gtMethod, x))
    def __ge__(self, x):
        return Opov(self._mcall2(self.geMethod, x))
    def __getitem__(self, x):
        return Opov(self._mcall2(self.getitemMethod, x))
    def __delitem__(self, x):
        return Opov(self._mcall2(self.delitemMethod, x))
    def __pow__(self, x, y=''):
        if y:
            ys = ', ' + str(y)
        else:
            ys = ''
        return Opov(self.x + '.__pow__(' + str(x) + ys + ')')
    def __ipow__(self, x, y=''):
        if y:
            ys = ', ' + str(y)
        else:
            ys = ''
        return Opov(self.x + '.__ipow__(' + str(x) + ys + ')')
    def __call__(self, *args):
        z = ','.join(map(str, args))
        return Opov(self.x + '.__call__(' + z + ')')
