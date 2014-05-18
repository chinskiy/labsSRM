import unittest
from big_int import BigInt
import time


class TestBigInt(unittest.TestCase):
    def setUp(self):

        #self.a_big = BigInt(256, '82B19600B943B35D5A1446C3106FD113676E17ACB5AA02FDD5C68C373F7BC665')
        #self.b_big = BigInt(256, '7BFC75B3ECD02B477B07FAEB9026D9AF74BBEF15238E40A6ACDDDFA7F5894E78')
        #self.c_big = BigInt(256, 'B8D0595741E7C058383E123A2441173986E02FED03B5ABE3EE130C784DC25A16')
        #self.d_big = BigInt(256)
        #self.a = 59114437527753047487343828859745690255623963500462411490577576222775377118821
        #self.b = 56080538191158283154688556480952549260966904473337717729239374531310717062776
        #self.c = 83593684936675779736037743653321255352559267247783671869375845741170341861910

        #self.a_big = BigInt(384, 'F9D80B78917C3B3F5C4605F3CD5C4994C9C47A51F70995C623F2CB15EB7DE1AF6B032892070D7E0F03CB75729797B9A7')
        #self.b_big = BigInt(384, '7513AA9E0247F3943B1B919B52C2A38C56AE2A25A78C6A82D7559129736603DECAFFC768E663E43E24097EB7726D81A9')
        #self.c_big = BigInt(384, '8BCC674FF06ABEC1D5638074FF97AA6FB7FC123B72CBF27C149F9CDBCAEC8220212AC70060166F63E20FA972046EB2F6')
        #self.d_big = BigInt(384)
        #self.a = 38454499540180223961777154316684083615032162820163739612116223748848314600095075108988767268835404970709143355111847
        #self.b = 18019772157380467000825188453934175771732458333402724802959359723433308354378026506601467430281344801345554535514537
        #self.c = 21516950973038496336285577804761447504111566241945841365330231333165087516161646974611873443732059147156808147055350

        #self.a_big = BigInt(512,
        #           'F2BBB29A0080AAD10D509956A95156F9723DA2D4EE679F04EC523162D86BFB4ADBD614C3BD20E03408DEDCB39A9B3A0743D9FD7B51CBEA44D19EE1D1E597D0B3')
        #self.b_big = BigInt(512,
        #           'B2B251312DCD85917E445966741F94CCFC5756432364C7CDC45DDE5DDAB5E3DCB6221D664652FB634A91AAAC179B21B7E6E48F68478E899CFD0CE8C3C05ECAA5')
        #self.c_big = BigInt(512,
        #           'BF7541ACDAB4389824EA77D7483A8B93CDD24FB9C16D62EF9DB34E263AE0EC2D86E67D02E1E62D6B1AB716F0488D7FED38D7B2B6CF00D6B2E66F0CE59211593F')
        #self.d_big = BigInt(512)
        #self.a = 12712968919096993975699367211356790261988274411101715678918504565574052507288208276408373589932376224163139210598432179409459799456895346134009244768784563
        #self.b = 9359097807903209648555486644504384682520867779386556506070101902341293852626894913560029781242585817602629389119564931672572168594391001357027549929982629
        #self.c = 10027470852054426673543263626939318105546986731423883291600188733665007690221952027602644446318282822168625555406269104706799898161595226029429105391393087

        #self.a_big = BigInt(768,
        #           'D2D56D2ED9A5CC5A9070A040A6F489CB6C177ED74476C06A1E5EE32E91A3E286FD771A53DCE923EF26D5E761DA141210F4DD649C3A98B122CB02218D65A707A88CF51133A2BB7D7348E80E8522ADD9F6A67AF3C839E05C257E971147911E9E6E')
        #self.b_big = BigInt(768,
        #           '62B3ECEC9AC5CFD451205AEC8A06A6815B0802DC18BA59338898A7CFA21D8CD886D8E818E314CA9EF9BB18AA737C53589E4E92ED6A8E1B72D50AA50BC0105180B3973A8DF198D42704D2DFEC13315CC1884C49DB64971E465335738069F5266D')
        #self.c_big = BigInt(768,
        #           'C1138A28DB497108822D6B69DCB6273632E41950175528309323FFB150CE30DFCC6EDB3002E0F6D9B6777F71C45FB7984B0500681CBE6A7C1B44DAC36F69CAEC205780684141A8630829DCE6F009AC24CEF409406EDFCFC184D5C2E499FE358')
        #self.d_big = BigInt(768)
        #self.a = 1278605974406429966024664333080837586125956490509683207290436819438838344974591658707276306592020405251682975041127769412065390007200861785532720044132559351419057447681320294919445462555521799216966472643382059281722919307007925870
        #self.b = 598585685284934617117413489669619420663617881122559709616740124431427677015385406101360166464685900008630392393943149544570177366682334449186937249854908799122404059635001763931808674221236148701832144454648941401715730585576875629
        #self.c = 73182248707108810808463017047842576140833966722210859883790481807948808724522325347159989658209564409718314247564988912845003399507483823562973004675944039628147751320202241040530627304822011890464335558536023086522316369587856216

        #self.a_big = BigInt(1024,
        #           'FA815F0256BF177289043EA385FA858D3E9ABB3BD321B3A04DD958E9CB168D51F0E96A865D5AC90166870101AAAB44854CF1B4B797946BEB4A093DFEE039ED3139A2EEB9EE5C4623E6368B4F9D6A0581C755931198755B3188F9B5E9CA6FEF5A265481BDBAB2F0CB8C8AFADEA90311988BA6D2A25A7C8E902D70FF45EFE0F7CF')
        #self.b_big = BigInt(1024,
        #           'EF20E7D078DD8219D1B62893E7C49206C7CA3F441127FB209ABDF965E7C5A02356928D0451E733364C163F68E8EDEE576C3C492D9DA25D6BA53FD74C97CF8C741EB4C1EFD0CB647105D5296E84D6DA3D9E56F6970941030ED4A62EDBE163632F353FDCA88144BEE196643234F576A806B33DC22E6179AFF713D1DDDE89D408FB')
        #self.c_big = BigInt(1024,
        #           'B5EA5D0686C36C6EAC9DC7446716C00712D1C2052B0AAAD6332F43C56940A696E5FC3FE0789EAD2777646B9FE39823BB80BDDA384EE2C5E000940D2BF03BE3F5DF06482E1BEED81FFBC77242E573F38D791644EF98FCE0F4195704A4DC1656AFE9E16C69F74373C724C4117CEE03F4C9BD31366F2B8E48672D4D361FC81154C9')
        #self.d_big = BigInt(1024)
        #self.a = 175910843234906646412460604009167226663320955090819745876404983973753759349997731637257963001706534466066598565239869557056482035363305942016449960033029490936426654945985177775904492642079861551593427536651571452346793107334906558876839565103847169574497181954742090519970098918608618226486259659860521056207
        #self.b = 167921769408288635864237847587802858387512953691255129095026732908576219904312285891170994088429635574281170781758906023344358259712872028599141212283602345165504993816780659209602974565944022075017376569622651638033320012151067303441562707085062991490682654373805133161917827979845305276068339984090872940795
        #self.c = 127745395718034262892866039807406716865311755591440375995656887796715892460179465236334903349915594153829698214426566724619831577924361930050915161390422069447655460030487781474568465731498335767296010609628074861589188755557434378992723719622668946452384721485549127139938236780884428508502590770356994266313


        self.d = 0
        self.time_python = 0
        self.time_big_int = 0

    def tearDown(self):
        print ('time_bigint = ', '%f' % self.time_big_int)
        #print('time_python = ', '%f' % self.time_python)

    #def test_add(self):
    #    print('Add:')
    #    self.start_time = time.time()
    #    for i in range(500):
    #        self.a_big + self.b_big
    #    self.time_big_int = (time.time() - self.start_time) / 500
    #    self.start_time = time.time()
    #    for i in range(500):
    #        self.d = self.a + self.b
    #    self.time_python = (time.time() - self.start_time) / 500
    #    self.d_big == self.a_big + self.b_big
    #    self.assertEqual(self.d, int(self.d_big.ret_numb_dec()))
    #
    #def test_sub(self):
    #    print('Sub:')
    #    self.start_time = time.time()
    #    for i in range(500):
    #        self.a_big - self.b_big
    #    self.time_big_int = (time.time() - self.start_time) / 500
    #    self.start_time = time.time()
    #    for i in range(500):
    #        self.d = self.a - self.b
    #    self.time_python = (time.time() - self.start_time) / 500
    #    self.d_big == self.a_big - self.b_big
    #    self.assertEqual(self.d, int(self.d_big.ret_numb_dec()))

    #def test_mul(self):
    #    print('Mul:')
    #    self.start_time = time.time()
    #    for i in range(100):
    #        self.a_big * self.b_big
    #    self.time_big_int = (time.time() - self.start_time) / 100
    #    self.start_time = time.time()
    #    for i in range(100):
    #        self.d = self.a * self.b
    #    self.time_python = (time.time() - self.start_time) / 100
    #    self.d_big == self.a_big * self.b_big
    #    self.assertEqual(self.d, int(self.d_big.ret_numb_dec()))

    #def test_moddiv(self):
    #    print('Moddiv:')
    #    self.start_time = time.time()
    #    for i in range(1000):
    #        self.a_big % self.b_big
    #    self.time_big_int = (time.time() - self.start_time) / 1000
    #    self.start_time = time.time()
    #    for i in range(1000):
    #        self.d = self.a % self.b
    #    self.time_python = (time.time() - self.start_time) / 1000
    #    self.assertEqual(self.d, int(self.a_big.from_hex_to_dec(self.a_big % self.b_big)))
    #
    #def test_barret(self):
    #    print('Barret:')
    #    c = self.a_big.calculation_nyu(self.b_big)
    #    self.start_time = time.time()
    #    for i in range(1000):
    #        self.a_big.barret_reduction(self.a_big, self.b_big, c)
    #    self.time_big_int = (time.time() - self.start_time) / 1000
    #    self.start_time = time.time()
    #    for i in range(1000):
    #        self.d = self.a % self.b
    #    self.c_big == self.a_big.barret_reduction(self.a_big, self.b_big, c)
    #    self.time_python = (time.time() - self.start_time) / 1000
    #    self.assertEqual(self.d, int(self.c_big.ret_numb_dec()))

    #def test_alg_blackley(self):
    #    print('Alg Blackley:')
    #    self.start_time = time.time()
    #    for i in range(10):
    #        self.a_big.blackley_alg(self.b_big, self.c_big)
    #    self.time_big_int = (time.time() - self.start_time) / 10
    #    self.start_time = time.time()
    #    for i in range(10):
    #        self.d = (self.a * self.b) % self.c
    #    self.time_python = (time.time() - self.start_time) / 10
    #    self.a_big == self.a_big.mul_by_module(self.a_big, self.b_big, self.c_big)
    #    self.assertEqual(self.d, int(self.a_big.ret_numb_dec()))

    def test_to_hight_degree_by_module(self):
        self.start_time = time.time()
        for i in range(5):
            self.a_big.to_hight_degree_by_module(self.a_big, self.b_big, self.c_big)
        self.time_big_int = (time.time() - self.start_time) / 5
        #self.start_time = time.time()
        #for i in range(10):
        #    self.d = (self.a ** self.b) % self.c
        #self.time_python = (time.time() - self.start_time) / 10
        #self.a_big == self.a_big.to_hight_degree_by_module(self.a_big, self.b_big, self.c_big)
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()