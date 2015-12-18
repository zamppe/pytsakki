from numpy import uint64
##knightmoves = []
##knightmoves.append(uint64(0x20400L))
##knightmoves.append(uint64(0x50800L))
##knightmoves.append(uint64(0xa1100L))
##knightmoves.append(uint64(0x142200L))
##knightmoves.append(uint64(0x284400L))
##knightmoves.append(uint64(0x508800L))
##knightmoves.append(uint64(0xa01000L))
##knightmoves.append(uint64(0x402000L))
##knightmoves.append(uint64(0x2040004L))
##knightmoves.append(uint64(0x5080008L))
##knightmoves.append(uint64(0xa110011L))
##knightmoves.append(uint64(0x14220022L))
##knightmoves.append(uint64(0x28440044L))
##knightmoves.append(uint64(0x50880088L))
##knightmoves.append(uint64(0xa0100010L))
##knightmoves.append(uint64(0x40200020L))
##knightmoves.append(uint64(0x204000402L))
##knightmoves.append(uint64(0x508000805L))
##knightmoves.append(uint64(0xa1100110aL))
##knightmoves.append(uint64(0x1422002214L))
##knightmoves.append(uint64(0x2844004428L))
##knightmoves.append(uint64(0x5088008850L))
##knightmoves.append(uint64(0xa0100010a0L))
##knightmoves.append(uint64(0x4020002040L))
##knightmoves.append(uint64(0x20400040200L))
##knightmoves.append(uint64(0x50800080500L))
##knightmoves.append(uint64(0xa1100110a00L))
##knightmoves.append(uint64(0x142200221400L))
##knightmoves.append(uint64(0x284400442800L))
##knightmoves.append(uint64(0x508800885000L))
##knightmoves.append(uint64(0xa0100010a000L))
##knightmoves.append(uint64(0x402000204000L))
##knightmoves.append(uint64(0x2040004020000L))
##knightmoves.append(uint64(0x5080008050000L))
##knightmoves.append(uint64(0xa1100110a0000L))
##knightmoves.append(uint64(0x14220022140000L))
##knightmoves.append(uint64(0x28440044280000L))
##knightmoves.append(uint64(0x50880088500000L))
##knightmoves.append(uint64(0xa0100010a00000L))
##knightmoves.append(uint64(0x40200020400000L))
##knightmoves.append(uint64(0x204000402000000L))
##knightmoves.append(uint64(0x508000805000000L))
##knightmoves.append(uint64(0xa1100110a000000L))
##knightmoves.append(uint64(0x1422002214000000L))
##knightmoves.append(uint64(0x2844004428000000L))
##knightmoves.append(uint64(0x5088008850000000L))
##knightmoves.append(uint64(0xa0100010a0000000L))
##knightmoves.append(uint64(0x4020002040000000L))
##knightmoves.append(uint64(0x400040200000000L))
##knightmoves.append(uint64(0x800080500000000L))
##knightmoves.append(uint64(0x1100110a00000000L))
##knightmoves.append(uint64(0x2200221400000000L))
##knightmoves.append(uint64(0x4400442800000000L))
##knightmoves.append(uint64(0x8800885000000000L))
##knightmoves.append(uint64(0x100010a000000000L))
##knightmoves.append(uint64(0x2000204000000000L))
##knightmoves.append(uint64(0x4020000000000L))
##knightmoves.append(uint64(0x8050000000000L))
##knightmoves.append(uint64(0x110a0000000000L))
##knightmoves.append(uint64(0x22140000000000L))
##knightmoves.append(uint64(0x44280000000000L))
##knightmoves.append(uint64(0x88500000000000L))
##knightmoves.append(uint64(0x10a00000000000L))
##knightmoves.append(uint64(0x20400000000000L))
##
##bishopattacks = [0]*64
##bishopattacks[0] = uint64(9241421688590303744)
##bishopattacks[1] = uint64(36099303471056128)
##bishopattacks[2] = uint64(141012904249856)
##bishopattacks[3] = uint64(550848566272)
##bishopattacks[4] = uint64(6480472064)
##bishopattacks[5] = uint64(1108177604608)
##bishopattacks[6] = uint64(283691315142656)
##bishopattacks[7] = uint64(72624976668147712)
##bishopattacks[8] = uint64(4620710844295151618)
##bishopattacks[9] = uint64(9241421688590368773)
##bishopattacks[10] = uint64(36099303487963146)
##bishopattacks[11] = uint64(141017232965652)
##bishopattacks[12] = uint64(1659000848424)
##bishopattacks[13] = uint64(283693466779728)
##bishopattacks[14] = uint64(72624976676520096)
##bishopattacks[15] = uint64(145249953336262720)
##bishopattacks[16] = uint64(2310355422147510788)
##bishopattacks[17] = uint64(4620710844311799048)
##bishopattacks[18] = uint64(9241421692918565393)
##bishopattacks[19] = uint64(36100411639206946)
##bishopattacks[20] = uint64(424704217196612)
##bishopattacks[21] = uint64(72625527495610504)
##bishopattacks[22] = uint64(145249955479592976)
##bishopattacks[23] = uint64(290499906664153120)
##bishopattacks[24] = uint64(1155177711057110024)
##bishopattacks[25] = uint64(2310355426409252880)
##bishopattacks[26] = uint64(4620711952330133792)
##bishopattacks[27] = uint64(9241705379636978241)
##bishopattacks[28] = uint64(108724279602332802)
##bishopattacks[29] = uint64(145390965166737412)
##bishopattacks[30] = uint64(290500455356698632)
##bishopattacks[31] = uint64(580999811184992272)
##bishopattacks[32] = uint64(577588851267340304)
##bishopattacks[33] = uint64(1155178802063085600)
##bishopattacks[34] = uint64(2310639079102947392)
##bishopattacks[35] = uint64(4693335752243822976)
##bishopattacks[36] = uint64(9386671504487645697)
##bishopattacks[37] = uint64(326598935265674242)
##bishopattacks[38] = uint64(581140276476643332)
##bishopattacks[39] = uint64(1161999073681608712)
##bishopattacks[40] = uint64(288793334762704928)
##bishopattacks[41] = uint64(577868148797087808)
##bishopattacks[42] = uint64(1227793891648880768)
##bishopattacks[43] = uint64(2455587783297826816)
##bishopattacks[44] = uint64(4911175566595588352)
##bishopattacks[45] = uint64(9822351133174399489)
##bishopattacks[46] = uint64(1197958188344280066)
##bishopattacks[47] = uint64(2323857683139004420)
##bishopattacks[48] = uint64(144117404414255168)
##bishopattacks[49] = uint64(360293502378066048)
##bishopattacks[50] = uint64(720587009051099136)
##bishopattacks[51] = uint64(1441174018118909952)
##bishopattacks[52] = uint64(2882348036221108224)
##bishopattacks[53] = uint64(5764696068147249408)
##bishopattacks[54] = uint64(11529391036782871041)
##bishopattacks[55] = uint64(4611756524879479810)
##bishopattacks[56] = uint64(567382630219904)
##bishopattacks[57] = uint64(1416240237150208)
##bishopattacks[58] = uint64(2833579985862656)
##bishopattacks[59] = uint64(5667164249915392)
##bishopattacks[60] = uint64(11334324221640704)
##bishopattacks[61] = uint64(22667548931719168)
##bishopattacks[62] = uint64(45053622886727936)
##bishopattacks[63] = uint64(18049651735527937)
##
##rookattacks = [0]*64
##rookattacks[0] = uint64(72340172838076926)
##rookattacks[1] = uint64(144680345676153597)
##rookattacks[2] = uint64(289360691352306939)
##rookattacks[3] = uint64(578721382704613623)
##rookattacks[4] = uint64(1157442765409226991)
##rookattacks[5] = uint64(2314885530818453727)
##rookattacks[6] = uint64(4629771061636907199)
##rookattacks[7] = uint64(9259542123273814143)
##rookattacks[8] = uint64(72340172838141441)
##rookattacks[9] = uint64(144680345676217602)
##rookattacks[10] = uint64(289360691352369924)
##rookattacks[11] = uint64(578721382704674568)
##rookattacks[12] = uint64(1157442765409283856)
##rookattacks[13] = uint64(2314885530818502432)
##rookattacks[14] = uint64(4629771061636939584)
##rookattacks[15] = uint64(9259542123273813888)
##rookattacks[16] = uint64(72340172854657281)
##rookattacks[17] = uint64(144680345692602882)
##rookattacks[18] = uint64(289360691368494084)
##rookattacks[19] = uint64(578721382720276488)
##rookattacks[20] = uint64(1157442765423841296)
##rookattacks[21] = uint64(2314885530830970912)
##rookattacks[22] = uint64(4629771061645230144)
##rookattacks[23] = uint64(9259542123273748608)
##rookattacks[24] = uint64(72340177082712321)
##rookattacks[25] = uint64(144680349887234562)
##rookattacks[26] = uint64(289360695496279044)
##rookattacks[27] = uint64(578721386714368008)
##rookattacks[28] = uint64(1157442769150545936)
##rookattacks[29] = uint64(2314885534022901792)
##rookattacks[30] = uint64(4629771063767613504)
##rookattacks[31] = uint64(9259542123257036928)
##rookattacks[32] = uint64(72341259464802561)
##rookattacks[33] = uint64(144681423712944642)
##rookattacks[34] = uint64(289361752209228804)
##rookattacks[35] = uint64(578722409201797128)
##rookattacks[36] = uint64(1157443723186933776)
##rookattacks[37] = uint64(2314886351157207072)
##rookattacks[38] = uint64(4629771607097753664)
##rookattacks[39] = uint64(9259542118978846848)
##rookattacks[40] = uint64(72618349279904001)
##rookattacks[41] = uint64(144956323094725122)
##rookattacks[42] = uint64(289632270724367364)
##rookattacks[43] = uint64(578984165983651848)
##rookattacks[44] = uint64(1157687956502220816)
##rookattacks[45] = uint64(2315095537539358752)
##rookattacks[46] = uint64(4629910699613634624)
##rookattacks[47] = uint64(9259541023762186368)
##rookattacks[48] = uint64(143553341945872641)
##rookattacks[49] = uint64(215330564830528002)
##rookattacks[50] = uint64(358885010599838724)
##rookattacks[51] = uint64(645993902138460168)
##rookattacks[52] = uint64(1220211685215703056)
##rookattacks[53] = uint64(2368647251370188832)
##rookattacks[54] = uint64(4665518383679160384)
##rookattacks[55] = uint64(9259260648297103488)
##rookattacks[56] = uint64(18302911464433844481)
##rookattacks[57] = uint64(18231136449196065282)
##rookattacks[58] = uint64(18087586418720506884)
##rookattacks[59] = uint64(17800486357769390088)
##rookattacks[60] = uint64(17226286235867156496)
##rookattacks[61] = uint64(16077885992062689312)
##rookattacks[62] = uint64(13781085504453754944)
##rookattacks[63] = uint64(9187484529235886208)
##
##queenattacks = [0]*64
##queenattacks[0] = uint64(9313761861428380670)
##queenattacks[1] = uint64(180779649147209725)
##queenattacks[2] = uint64(289501704256556795)
##queenattacks[3] = uint64(578721933553179895)
##queenattacks[4] = uint64(1157442771889699055)
##queenattacks[5] = uint64(2314886638996058335)
##queenattacks[6] = uint64(4630054752952049855)
##queenattacks[7] = uint64(9332167099941961855)
##queenattacks[8] = uint64(4693051017133293059)
##queenattacks[9] = uint64(9386102034266586375)
##queenattacks[10] = uint64(325459994840333070)
##queenattacks[11] = uint64(578862399937640220)
##queenattacks[12] = uint64(1157444424410132280)
##queenattacks[13] = uint64(2315169224285282160)
##queenattacks[14] = uint64(4702396038313459680)
##queenattacks[15] = uint64(9404792076610076608)
##queenattacks[16] = uint64(2382695595002168069)
##queenattacks[17] = uint64(4765391190004401930)
##queenattacks[18] = uint64(9530782384287059477)
##queenattacks[19] = uint64(614821794359483434)
##queenattacks[20] = uint64(1157867469641037908)
##queenattacks[21] = uint64(2387511058326581416)
##queenattacks[22] = uint64(4775021017124823120)
##queenattacks[23] = uint64(9550042029937901728)
##queenattacks[24] = uint64(1227517888139822345)
##queenattacks[25] = uint64(2455035776296487442)
##queenattacks[26] = uint64(4910072647826412836)
##queenattacks[27] = uint64(9820426766351346249)
##queenattacks[28] = uint64(1266167048752878738)
##queenattacks[29] = uint64(2460276499189639204)
##queenattacks[30] = uint64(4920271519124312136)
##queenattacks[31] = uint64(9840541934442029200)
##queenattacks[32] = uint64(649930110732142865)
##queenattacks[33] = uint64(1299860225776030242)
##queenattacks[34] = uint64(2600000831312176196)
##queenattacks[35] = uint64(5272058161445620104)
##queenattacks[36] = uint64(10544115227674579473)
##queenattacks[37] = uint64(2641485286422881314)
##queenattacks[38] = uint64(5210911883574396996)
##queenattacks[39] = uint64(10421541192660455560)
##queenattacks[40] = uint64(361411684042608929)
##queenattacks[41] = uint64(722824471891812930)
##queenattacks[42] = uint64(1517426162373248132)
##queenattacks[43] = uint64(3034571949281478664)
##queenattacks[44] = uint64(6068863523097809168)
##queenattacks[45] = uint64(12137446670713758241)
##queenattacks[46] = uint64(5827868887957914690)
##queenattacks[47] = uint64(11583398706901190788)
##queenattacks[48] = uint64(287670746360127809)
##queenattacks[49] = uint64(575624067208594050)
##queenattacks[50] = uint64(1079472019650937860)
##queenattacks[51] = uint64(2087167920257370120)
##queenattacks[52] = uint64(4102559721436811280)
##queenattacks[53] = uint64(8133343319517438240)
##queenattacks[54] = uint64(16194909420462031425)
##queenattacks[55] = uint64(13871017173176583298)
##queenattacks[56] = uint64(18303478847064064385)
##queenattacks[57] = uint64(18232552689433215490)
##queenattacks[58] = uint64(18090419998706369540)
##queenattacks[59] = uint64(17806153522019305480)
##queenattacks[60] = uint64(17237620560088797200)
##queenattacks[61] = uint64(16100553540994408480)
##queenattacks[62] = uint64(13826139127340482880)
##queenattacks[63] = uint64(9205534180971414145)

northattacks = []
northattacks.append(uint64(72340172838076672L))
northattacks.append(uint64(144680345676153344L))
northattacks.append(uint64(289360691352306688L))
northattacks.append(uint64(578721382704613376L))
northattacks.append(uint64(1157442765409226752L))
northattacks.append(uint64(2314885530818453504L))
northattacks.append(uint64(4629771061636907008L))
northattacks.append(uint64(9259542123273814016L))
northattacks.append(uint64(72340172838076416L))
northattacks.append(uint64(144680345676152832L))
northattacks.append(uint64(289360691352305664L))
northattacks.append(uint64(578721382704611328L))
northattacks.append(uint64(1157442765409222656L))
northattacks.append(uint64(2314885530818445312L))
northattacks.append(uint64(4629771061636890624L))
northattacks.append(uint64(9259542123273781248L))
northattacks.append(uint64(72340172838010880L))
northattacks.append(uint64(144680345676021760L))
northattacks.append(uint64(289360691352043520L))
northattacks.append(uint64(578721382704087040L))
northattacks.append(uint64(1157442765408174080L))
northattacks.append(uint64(2314885530816348160L))
northattacks.append(uint64(4629771061632696320L))
northattacks.append(uint64(9259542123265392640L))
northattacks.append(uint64(72340172821233664L))
northattacks.append(uint64(144680345642467328L))
northattacks.append(uint64(289360691284934656L))
northattacks.append(uint64(578721382569869312L))
northattacks.append(uint64(1157442765139738624L))
northattacks.append(uint64(2314885530279477248L))
northattacks.append(uint64(4629771060558954496L))
northattacks.append(uint64(9259542121117908992L))
northattacks.append(uint64(72340168526266368L))
northattacks.append(uint64(144680337052532736L))
northattacks.append(uint64(289360674105065472L))
northattacks.append(uint64(578721348210130944L))
northattacks.append(uint64(1157442696420261888L))
northattacks.append(uint64(2314885392840523776L))
northattacks.append(uint64(4629770785681047552L))
northattacks.append(uint64(9259541571362095104L))
northattacks.append(uint64(72339069014638592L))
northattacks.append(uint64(144678138029277184L))
northattacks.append(uint64(289356276058554368L))
northattacks.append(uint64(578712552117108736L))
northattacks.append(uint64(1157425104234217472L))
northattacks.append(uint64(2314850208468434944L))
northattacks.append(uint64(4629700416936869888L))
northattacks.append(uint64(9259400833873739776L))
northattacks.append(uint64(72057594037927936L))
northattacks.append(uint64(144115188075855872L))
northattacks.append(uint64(288230376151711744L))
northattacks.append(uint64(576460752303423488L))
northattacks.append(uint64(1152921504606846976L))
northattacks.append(uint64(2305843009213693952L))
northattacks.append(uint64(4611686018427387904L))
northattacks.append(uint64(9223372036854775808L))
northattacks.append(uint64(0L))
northattacks.append(uint64(0L))
northattacks.append(uint64(0L))
northattacks.append(uint64(0L))
northattacks.append(uint64(0L))
northattacks.append(uint64(0L))
northattacks.append(uint64(0L))
northattacks.append(uint64(0L))

southattacks = [0]*64
southattacks[63] = uint64(36170086419038336L)
southattacks[62] = uint64(18085043209519168L)
southattacks[61] = uint64(9042521604759584L)
southattacks[60] = uint64(4521260802379792L)
southattacks[59] = uint64(2260630401189896L)
southattacks[58] = uint64(1130315200594948L)
southattacks[57] = uint64(565157600297474L)
southattacks[56] = uint64(282578800148737L)
southattacks[55] = uint64(141289400074368L)
southattacks[54] = uint64(70644700037184L)
southattacks[53] = uint64(35322350018592L)
southattacks[52] = uint64(17661175009296L)
southattacks[51] = uint64(8830587504648L)
southattacks[50] = uint64(4415293752324L)
southattacks[49] = uint64(2207646876162L)
southattacks[48] = uint64(1103823438081L)
southattacks[47] = uint64(551911719040L)
southattacks[46] = uint64(275955859520L)
southattacks[45] = uint64(137977929760L)
southattacks[44] = uint64(68988964880L)
southattacks[43] = uint64(34494482440L)
southattacks[42] = uint64(17247241220L)
southattacks[41] = uint64(8623620610L)
southattacks[40] = uint64(4311810305L)
southattacks[39] = uint64(2155905152L)
southattacks[38] = uint64(1077952576L)
southattacks[37] = uint64(538976288L)
southattacks[36] = uint64(269488144L)
southattacks[35] = uint64(134744072L)
southattacks[34] = uint64(67372036L)
southattacks[33] = uint64(33686018L)
southattacks[32] = uint64(16843009L)
southattacks[31] = uint64(8421504L)
southattacks[30] = uint64(4210752L)
southattacks[29] = uint64(2105376L)
southattacks[28] = uint64(1052688L)
southattacks[27] = uint64(526344L)
southattacks[26] = uint64(263172L)
southattacks[25] = uint64(131586L)
southattacks[24] = uint64(65793L)
southattacks[23] = uint64(32896L)
southattacks[22] = uint64(16448L)
southattacks[21] = uint64(8224L)
southattacks[20] = uint64(4112L)
southattacks[19] = uint64(2056L)
southattacks[18] = uint64(1028L)
southattacks[17] = uint64(514L)
southattacks[16] = uint64(257L)
southattacks[15] = uint64(128L)
southattacks[14] = uint64(64L)
southattacks[13] = uint64(32L)
southattacks[12] = uint64(16L)
southattacks[11] = uint64(8L)
southattacks[10] = uint64(4L)
southattacks[9] = uint64(2L)
southattacks[8] = uint64(1L)
southattacks[7] = uint64(0L)
southattacks[6] = uint64(0L)
southattacks[5] = uint64(0L)
southattacks[4] = uint64(0L)
southattacks[3] = uint64(0L)
southattacks[2] = uint64(0L)
southattacks[1] = uint64(0L)
southattacks[0] = uint64(0L)

westattacks = [0]*64
westattacks[0] = uint64(254)
westattacks[8] = uint64(65024)
westattacks[16] = uint64(16646144)
westattacks[24] = uint64(4261412864)
westattacks[32] = uint64(1090921693184)
westattacks[40] = uint64(279275953455104)
westattacks[48] = uint64(71494644084506624)
westattacks[56] = uint64(18302628885633695744)
westattacks[1] = uint64(252)
westattacks[9] = uint64(64512)
westattacks[17] = uint64(16515072)
westattacks[25] = uint64(4227858432)
westattacks[33] = uint64(1082331758592)
westattacks[41] = uint64(277076930199552)
westattacks[49] = uint64(70931694131085312)
westattacks[57] = uint64(18158513697557839872)
westattacks[2] = uint64(248)
westattacks[10] = uint64(63488)
westattacks[18] = uint64(16252928)
westattacks[26] = uint64(4160749568)
westattacks[34] = uint64(1065151889408)
westattacks[42] = uint64(272678883688448)
westattacks[50] = uint64(69805794224242688)
westattacks[58] = uint64(17870283321406128128)
westattacks[3] = uint64(240)
westattacks[11] = uint64(61440)
westattacks[19] = uint64(15728640)
westattacks[27] = uint64(4026531840)
westattacks[35] = uint64(1030792151040)
westattacks[43] = uint64(263882790666240)
westattacks[51] = uint64(67553994410557440)
westattacks[59] = uint64(17293822569102704640)
westattacks[4] = uint64(224)
westattacks[12] = uint64(57344)
westattacks[20] = uint64(14680064)
westattacks[28] = uint64(3758096384)
westattacks[36] = uint64(962072674304)
westattacks[44] = uint64(246290604621824)
westattacks[52] = uint64(63050394783186944)
westattacks[60] = uint64(16140901064495857664)
westattacks[5] = uint64(192)
westattacks[13] = uint64(49152)
westattacks[21] = uint64(12582912)
westattacks[29] = uint64(3221225472)
westattacks[37] = uint64(824633720832)
westattacks[45] = uint64(211106232532992)
westattacks[53] = uint64(54043195528445952)
westattacks[61] = uint64(13835058055282163712)
westattacks[6] = uint64(128)
westattacks[14] = uint64(32768)
westattacks[22] = uint64(8388608)
westattacks[30] = uint64(2147483648)
westattacks[38] = uint64(549755813888)
westattacks[46] = uint64(140737488355328)
westattacks[54] = uint64(36028797018963968)
westattacks[62] = uint64(9223372036854775808)
westattacks[7] = uint64(0)
westattacks[15] = uint64(0)
westattacks[23] = uint64(0)
westattacks[31] = uint64(0)
westattacks[39] = uint64(0)
westattacks[47] = uint64(0)
westattacks[55] = uint64(0)
westattacks[63] = uint64(0)

eastattacks = [0]*64
eastattacks[63] = uint64(9151314442816847872)
eastattacks[55] = uint64(35747322042253312)
eastattacks[47] = uint64(139637976727552)
eastattacks[39] = uint64(545460846592)
eastattacks[31] = uint64(2130706432)
eastattacks[23] = uint64(8323072)
eastattacks[15] = uint64(32512)
eastattacks[7] = uint64(127)
eastattacks[62] = uint64(4539628424389459968)
eastattacks[54] = uint64(17732923532771328)
eastattacks[46] = uint64(69269232549888)
eastattacks[38] = uint64(270582939648)
eastattacks[30] = uint64(1056964608)
eastattacks[22] = uint64(4128768)
eastattacks[14] = uint64(16128)
eastattacks[6] = uint64(63)
eastattacks[61] = uint64(2233785415175766016)
eastattacks[53] = uint64(8725724278030336)
eastattacks[45] = uint64(34084860461056)
eastattacks[37] = uint64(133143986176)
eastattacks[29] = uint64(520093696)
eastattacks[21] = uint64(2031616)
eastattacks[13] = uint64(7936)
eastattacks[5] = uint64(31)
eastattacks[60] = uint64(1080863910568919040)
eastattacks[52] = uint64(4222124650659840)
eastattacks[44] = uint64(16492674416640)
eastattacks[36] = uint64(64424509440)
eastattacks[28] = uint64(251658240)
eastattacks[20] = uint64(983040)
eastattacks[12] = uint64(3840)
eastattacks[4] = uint64(15)
eastattacks[59] = uint64(504403158265495552)
eastattacks[51] = uint64(1970324836974592)
eastattacks[43] = uint64(7696581394432)
eastattacks[35] = uint64(30064771072)
eastattacks[27] = uint64(117440512)
eastattacks[19] = uint64(458752)
eastattacks[11] = uint64(1792)
eastattacks[3] = uint64(7)
eastattacks[58] = uint64(216172782113783808)
eastattacks[50] = uint64(844424930131968)
eastattacks[42] = uint64(3298534883328)
eastattacks[34] = uint64(12884901888)
eastattacks[26] = uint64(50331648)
eastattacks[18] = uint64(196608)
eastattacks[10] = uint64(768)
eastattacks[2] = uint64(3)
eastattacks[57] = uint64(72057594037927936)
eastattacks[49] = uint64(281474976710656)
eastattacks[41] = uint64(1099511627776)
eastattacks[33] = uint64(4294967296)
eastattacks[25] = uint64(16777216)
eastattacks[17] = uint64(65536)
eastattacks[9] = uint64(256)
eastattacks[1] = uint64(1)
eastattacks[56] = uint64(0)
eastattacks[48] = uint64(0)
eastattacks[40] = uint64(0)
eastattacks[32] = uint64(0)
eastattacks[24] = uint64(0)
eastattacks[16] = uint64(0)
eastattacks[8] = uint64(0)
eastattacks[0] = uint64(0)

seattacks = [0]*64
seattacks[63] = uint64(18049651735527937)
seattacks[55] = uint64(70506452091906)
seattacks[47] = uint64(275415828484)
seattacks[39] = uint64(1075843080)
seattacks[31] = uint64(4202512)
seattacks[23] = uint64(16416)
seattacks[15] = uint64(64)
seattacks[7] = uint64(0)
seattacks[62] = uint64(9024825867763968)
seattacks[54] = uint64(35253226045953)
seattacks[46] = uint64(137707914242)
seattacks[38] = uint64(537921540)
seattacks[30] = uint64(2101256)
seattacks[22] = uint64(8208)
seattacks[14] = uint64(32)
seattacks[6] = uint64(0)
seattacks[61] = uint64(4512412933881856)
seattacks[53] = uint64(17626613022976)
seattacks[45] = uint64(68853957121)
seattacks[37] = uint64(268960770)
seattacks[29] = uint64(1050628)
seattacks[21] = uint64(4104)
seattacks[13] = uint64(16)
seattacks[5] = uint64(0)
seattacks[60] = uint64(2256206466908160)
seattacks[52] = uint64(8813306511360)
seattacks[44] = uint64(34426978560)
seattacks[36] = uint64(134480385)
seattacks[28] = uint64(525314)
seattacks[20] = uint64(2052)
seattacks[12] = uint64(8)
seattacks[4] = uint64(0)
seattacks[59] = uint64(1128103225065472)
seattacks[51] = uint64(4406653222912)
seattacks[43] = uint64(17213489152)
seattacks[35] = uint64(67240192)
seattacks[27] = uint64(262657)
seattacks[19] = uint64(1026)
seattacks[11] = uint64(4)
seattacks[3] = uint64(0)
seattacks[58] = uint64(564049465049088)
seattacks[50] = uint64(2203318222848)
seattacks[42] = uint64(8606711808)
seattacks[34] = uint64(33619968)
seattacks[26] = uint64(131328)
seattacks[18] = uint64(513)
seattacks[10] = uint64(2)
seattacks[2] = uint64(0)
seattacks[57] = uint64(281474976710656)
seattacks[49] = uint64(1099511627776)
seattacks[41] = uint64(4294967296)
seattacks[33] = uint64(16777216)
seattacks[25] = uint64(65536)
seattacks[17] = uint64(256)
seattacks[9] = uint64(1)
seattacks[1] = uint64(0)
seattacks[56] = uint64(0)
seattacks[48] = uint64(0)
seattacks[40] = uint64(0)
seattacks[32] = uint64(0)
seattacks[24] = uint64(0)
seattacks[16] = uint64(0)
seattacks[8] = uint64(0)
seattacks[0] = uint64(0)

swattacks = [0]*64
swattacks[56] = uint64(567382630219904)
swattacks[48] = uint64(2216338399296)
swattacks[40] = uint64(8657571872)
swattacks[32] = uint64(33818640)
swattacks[24] = uint64(132104)
swattacks[16] = uint64(516)
swattacks[8] = uint64(2)
swattacks[0] = uint64(0)
swattacks[57] = uint64(1134765260439552)
swattacks[49] = uint64(4432676798592)
swattacks[41] = uint64(17315143744)
swattacks[33] = uint64(67637280)
swattacks[25] = uint64(264208)
swattacks[17] = uint64(1032)
swattacks[9] = uint64(4)
swattacks[1] = uint64(0)
swattacks[58] = uint64(2269530520813568)
swattacks[50] = uint64(8865353596928)
swattacks[42] = uint64(34630287488)
swattacks[34] = uint64(135274560)
swattacks[26] = uint64(528416)
swattacks[18] = uint64(2064)
swattacks[10] = uint64(8)
swattacks[2] = uint64(0)
swattacks[59] = uint64(4539061024849920)
swattacks[51] = uint64(17730707128320)
swattacks[43] = uint64(69260574720)
swattacks[35] = uint64(270549120)
swattacks[27] = uint64(1056832)
swattacks[19] = uint64(4128)
swattacks[11] = uint64(16)
swattacks[3] = uint64(0)
swattacks[60] = uint64(9078117754732544)
swattacks[52] = uint64(35461397479424)
swattacks[44] = uint64(138521083904)
swattacks[36] = uint64(541097984)
swattacks[28] = uint64(2113664)
swattacks[20] = uint64(8256)
swattacks[12] = uint64(32)
swattacks[4] = uint64(0)
swattacks[61] = uint64(18155135997837312)
swattacks[53] = uint64(70918499991552)
swattacks[45] = uint64(277025390592)
swattacks[37] = uint64(1082130432)
swattacks[29] = uint64(4227072)
swattacks[21] = uint64(16512)
swattacks[13] = uint64(64)
swattacks[5] = uint64(0)
swattacks[62] = uint64(36028797018963968)
swattacks[54] = uint64(140737488355328)
swattacks[46] = uint64(549755813888)
swattacks[38] = uint64(2147483648)
swattacks[30] = uint64(8388608)
swattacks[22] = uint64(32768)
swattacks[14] = uint64(128)
swattacks[6] = uint64(0)
swattacks[63] = uint64(0)
swattacks[55] = uint64(0)
swattacks[47] = uint64(0)
swattacks[39] = uint64(0)
swattacks[31] = uint64(0)
swattacks[23] = uint64(0)
swattacks[15] = uint64(0)
swattacks[7] = uint64(0)

nwattacks = [0]*64
nwattacks[0] = uint64(9241421688590303744)
nwattacks[8] = uint64(4620710844295151616)
nwattacks[16] = uint64(2310355422147510272)
nwattacks[24] = uint64(1155177711056977920)
nwattacks[32] = uint64(577588851233521664)
nwattacks[40] = uint64(288793326105133056)
nwattacks[48] = uint64(144115188075855872)
nwattacks[56] = uint64(0)
nwattacks[1] = uint64(36099303471055872)
nwattacks[9] = uint64(9241421688590303232)
nwattacks[17] = uint64(4620710844295020544)
nwattacks[25] = uint64(2310355422113955840)
nwattacks[33] = uint64(1155177702467043328)
nwattacks[41] = uint64(577586652210266112)
nwattacks[49] = uint64(288230376151711744)
nwattacks[57] = uint64(0)
nwattacks[2] = uint64(141012904183808)
nwattacks[10] = uint64(36099303471054848)
nwattacks[18] = uint64(9241421688590041088)
nwattacks[26] = uint64(4620710844227911680)
nwattacks[34] = uint64(2310355404934086656)
nwattacks[42] = uint64(1155173304420532224)
nwattacks[50] = uint64(576460752303423488)
nwattacks[58] = uint64(0)
nwattacks[3] = uint64(550831656960)
nwattacks[11] = uint64(141012904181760)
nwattacks[19] = uint64(36099303470530560)
nwattacks[27] = uint64(9241421688455823360)
nwattacks[35] = uint64(4620710809868173312)
nwattacks[43] = uint64(2310346608841064448)
nwattacks[51] = uint64(1152921504606846976)
nwattacks[59] = uint64(0)
nwattacks[4] = uint64(2151686144)
nwattacks[12] = uint64(550831652864)
nwattacks[20] = uint64(141012903133184)
nwattacks[28] = uint64(36099303202095104)
nwattacks[36] = uint64(9241421619736346624)
nwattacks[44] = uint64(4620693217682128896)
nwattacks[52] = uint64(2305843009213693952)
nwattacks[60] = uint64(0)
nwattacks[5] = uint64(8404992)
nwattacks[13] = uint64(2151677952)
nwattacks[21] = uint64(550829555712)
nwattacks[29] = uint64(141012366262272)
nwattacks[37] = uint64(36099165763141632)
nwattacks[45] = uint64(9241386435364257792)
nwattacks[53] = uint64(4611686018427387904)
nwattacks[61] = uint64(0)
nwattacks[6] = uint64(32768)
nwattacks[14] = uint64(8388608)
nwattacks[22] = uint64(2147483648)
nwattacks[30] = uint64(549755813888)
nwattacks[38] = uint64(140737488355328)
nwattacks[46] = uint64(36028797018963968)
nwattacks[54] = uint64(9223372036854775808)
nwattacks[62] = uint64(0)
nwattacks[7] = uint64(0)
nwattacks[15] = uint64(0)
nwattacks[23] = uint64(0)
nwattacks[31] = uint64(0)
nwattacks[39] = uint64(0)
nwattacks[47] = uint64(0)
nwattacks[55] = uint64(0)
nwattacks[63] = uint64(0)

neattacks = [0]*64
neattacks[7] = uint64(72624976668147712)
neattacks[15] = uint64(145249953336262656)
neattacks[23] = uint64(290499906664136704)
neattacks[31] = uint64(580999811180789760)
neattacks[39] = uint64(1161999072605765632)
neattacks[47] = uint64(2323857407723175936)
neattacks[55] = uint64(4611686018427387904)
neattacks[63] = uint64(0)
neattacks[6] = uint64(283691315109888)
neattacks[14] = uint64(72624976668131328)
neattacks[22] = uint64(145249953332068352)
neattacks[30] = uint64(290499905590394880)
neattacks[38] = uint64(580999536302882816)
neattacks[46] = uint64(1161928703861587968)
neattacks[54] = uint64(2305843009213693952)
neattacks[62] = uint64(0)
neattacks[5] = uint64(1108169199616)
neattacks[13] = uint64(283691315101696)
neattacks[21] = uint64(72624976666034176)
neattacks[29] = uint64(145249952795197440)
neattacks[37] = uint64(290499768151441408)
neattacks[45] = uint64(580964351930793984)
neattacks[53] = uint64(1152921504606846976)
neattacks[61] = uint64(0)
neattacks[4] = uint64(4328785920)
neattacks[12] = uint64(1108169195520)
neattacks[20] = uint64(283691314053120)
neattacks[28] = uint64(72624976397598720)
neattacks[36] = uint64(145249884075720704)
neattacks[44] = uint64(290482175965396992)
neattacks[52] = uint64(576460752303423488)
neattacks[60] = uint64(0)
neattacks[3] = uint64(16909312)
neattacks[11] = uint64(4328783872)
neattacks[19] = uint64(1108168671232)
neattacks[27] = uint64(283691179835392)
neattacks[35] = uint64(72624942037860352)
neattacks[43] = uint64(145241087982698496)
neattacks[51] = uint64(288230376151711744)
neattacks[59] = uint64(0)
neattacks[2] = uint64(66048)
neattacks[10] = uint64(16908288)
neattacks[18] = uint64(4328521728)
neattacks[26] = uint64(1108101562368)
neattacks[34] = uint64(283673999966208)
neattacks[42] = uint64(72620543991349248)
neattacks[50] = uint64(144115188075855872)
neattacks[58] = uint64(0)
neattacks[1] = uint64(256)
neattacks[9] = uint64(65536)
neattacks[17] = uint64(16777216)
neattacks[25] = uint64(4294967296)
neattacks[33] = uint64(1099511627776)
neattacks[41] = uint64(281474976710656)
neattacks[49] = uint64(72057594037927936)
neattacks[57] = uint64(0)
neattacks[0] = uint64(0)
neattacks[8] = uint64(0)
neattacks[16] = uint64(0)
neattacks[24] = uint64(0)
neattacks[32] = uint64(0)
neattacks[40] = uint64(0)
neattacks[48] = uint64(0)
neattacks[56] = uint64(0)


"""a list of 64 boards where only one bit is set"""
flags = []
flags.append(uint64(1L))
flags.append(uint64(2L))
flags.append(uint64(4L))
flags.append(uint64(8L))
flags.append(uint64(16L))
flags.append(uint64(32L))
flags.append(uint64(64L))
flags.append(uint64(128L))
flags.append(uint64(256L))
flags.append(uint64(512L))
flags.append(uint64(1024L))
flags.append(uint64(2048L))
flags.append(uint64(4096L))
flags.append(uint64(8192L))
flags.append(uint64(16384L))
flags.append(uint64(32768L))
flags.append(uint64(65536L))
flags.append(uint64(131072L))
flags.append(uint64(262144L))
flags.append(uint64(524288L))
flags.append(uint64(1048576L))
flags.append(uint64(2097152L))
flags.append(uint64(4194304L))
flags.append(uint64(8388608L))
flags.append(uint64(16777216L))
flags.append(uint64(33554432L))
flags.append(uint64(67108864L))
flags.append(uint64(134217728L))
flags.append(uint64(268435456L))
flags.append(uint64(536870912L))
flags.append(uint64(1073741824L))
flags.append(uint64(2147483648L))
flags.append(uint64(4294967296L))
flags.append(uint64(8589934592L))
flags.append(uint64(17179869184L))
flags.append(uint64(34359738368L))
flags.append(uint64(68719476736L))
flags.append(uint64(137438953472L))
flags.append(uint64(274877906944L))
flags.append(uint64(549755813888L))
flags.append(uint64(1099511627776L))
flags.append(uint64(2199023255552L))
flags.append(uint64(4398046511104L))
flags.append(uint64(8796093022208L))
flags.append(uint64(17592186044416L))
flags.append(uint64(35184372088832L))
flags.append(uint64(70368744177664L))
flags.append(uint64(140737488355328L))
flags.append(uint64(281474976710656L))
flags.append(uint64(562949953421312L))
flags.append(uint64(1125899906842624L))
flags.append(uint64(2251799813685248L))
flags.append(uint64(4503599627370496L))
flags.append(uint64(9007199254740992L))
flags.append(uint64(18014398509481984L))
flags.append(uint64(36028797018963968L))
flags.append(uint64(72057594037927936L))
flags.append(uint64(144115188075855872L))
flags.append(uint64(288230376151711744L))
flags.append(uint64(576460752303423488L))
flags.append(uint64(1152921504606846976L))
flags.append(uint64(2305843009213693952L))
flags.append(uint64(4611686018427387904L))
flags.append(uint64(9223372036854775808L))

coords = {}
##coords['1H'] = 0
##coords['1G'] = 1
##coords['1F'] = 2
##coords['1E'] = 3
##coords['1D'] = 4
##coords['1C'] = 5
##coords['1B'] = 6
##coords['1A'] = 7
##coords['2H'] = 8
##coords['2G'] = 9
##coords['2F'] = 10
##coords['2E'] = 11
##coords['2D'] = 12
##coords['2C'] = 13
##coords['2B'] = 14
##coords['2A'] = 15
##coords['3H'] = 16
##coords['3G'] = 17
##coords['3F'] = 18
##coords['3E'] = 19
##coords['3D'] = 20
##coords['3C'] = 21
##coords['3B'] = 22
##coords['3A'] = 23
##coords['4H'] = 24
##coords['4G'] = 25
##coords['4F'] = 26
##coords['4E'] = 27
##coords['4D'] = 28
##coords['4C'] = 29
##coords['4B'] = 30
##coords['4A'] = 31
##coords['5H'] = 32
##coords['5G'] = 33
##coords['5F'] = 34
##coords['5E'] = 35
##coords['5D'] = 36
##coords['5C'] = 37
##coords['5B'] = 38
##coords['5A'] = 39
##coords['6H'] = 40
##coords['6G'] = 41
##coords['6F'] = 42
##coords['6E'] = 43
##coords['6D'] = 44
##coords['6C'] = 45
##coords['6B'] = 46
##coords['6A'] = 47
##coords['7H'] = 48
##coords['7G'] = 49
##coords['7F'] = 50
##coords['7E'] = 51
##coords['7D'] = 52
##coords['7C'] = 53
##coords['7B'] = 54
##coords['7A'] = 55
##coords['8H'] = 56
##coords['8G'] = 57
##coords['8F'] = 58
##coords['8E'] = 59
##coords['8D'] = 60
##coords['8C'] = 61
##coords['8B'] = 62
##coords['8A'] = 63

coords[0] = 'H1'
coords[1] = 'G1'
coords[2] = 'F1'
coords[3] = 'E1'
coords[4] = 'D1'
coords[5] = 'C1'
coords[6] = 'B1'
coords[7] = 'A1'
coords[8] = 'H2'
coords[9] = 'G2'
coords[10] = 'F2'
coords[11] = 'E2'
coords[12] = 'D2'
coords[13] = 'C2'
coords[14] = 'B2'
coords[15] = 'A2'
coords[16] = 'H3'
coords[17] = 'G3'
coords[18] = 'F3'
coords[19] = 'E3'
coords[20] = 'D3'
coords[21] = 'C3'
coords[22] = 'B3'
coords[23] = 'A3'
coords[24] = 'H4'
coords[25] = 'G4'
coords[26] = 'F4'
coords[27] = 'E4'
coords[28] = 'D4'
coords[29] = 'C4'
coords[30] = 'B4'
coords[31] = 'A4'
coords[32] = 'H5'
coords[33] = 'G5'
coords[34] = 'F5'
coords[35] = 'E5'
coords[36] = 'D5'
coords[37] = 'C5'
coords[38] = 'B5'
coords[39] = 'A5'
coords[40] = 'H6'
coords[41] = 'G6'
coords[42] = 'F6'
coords[43] = 'E6'
coords[44] = 'D6'
coords[45] = 'C6'
coords[46] = 'B6'
coords[47] = 'A6'
coords[48] = 'H7'
coords[49] = 'G7'
coords[50] = 'F7'
coords[51] = 'E7'
coords[52] = 'D7'
coords[53] = 'C7'
coords[54] = 'B7'
coords[55] = 'A7'
coords[56] = 'H8'
coords[57] = 'G8'
coords[58] = 'F8'
coords[59] = 'E8'
coords[60] = 'D8'
coords[61] = 'C8'
coords[62] = 'B8'
coords[63] = 'A8'

piece_value = [0,0,0,100,100,350,350,350,350,500,500,800,800, 1000, 1000]
special_values = {'check' : 80,'mate': 10000, 'castling' : 200, 'promote': 700}

MOVE_VALUE_PAWN  = [0, 0, 0,  0,  0,  0,  0,  0,
                    50, 50, 50, 50, 50, 50, 50, 50,
                    10, 10, 20, 30, 30, 20, 10, 10,
                     5,  5, 10, 25, 25, 10,  5,  5,
                     0,  0,  0, 20, 20,  0,  0,  0,
                     5, -5,-10,  0,  0,-10, -5,  5,
                     5, 10, 10,-20,-20, 10, 10,  5,
                     0,  0,  0,  0,  0,  0,  0,  0 ]     
                         
MOVE_VALUE_KNIGHT = [-50,-40,-30,-30,-30,-30,-40,-50,
                     -40,-20,  0,  0,  0,  0,-20,-40,
                     -30,  0, 10, 15, 15, 10,  0,-30,
                     -30,  5, 15, 20, 20, 15,  5,-30,
                     -30,  0, 15, 20, 20, 15,  0,-30,
                     -30,  5, 10, 15, 15, 10,  5,-30,
                     -40,-20,  0,  5,  5,  0,-20,-40,
                     -50,-40,-30,-30,-30,-30,-40,-50 ] 
                            
MOVE_VALUE_BISHOP = [-20,-10,-10,-10,-10,-10,-10,-20,
                     -10,  0,  0,  0,  0,  0,  0,-10,
                     -10,  0,  5, 10, 10,  5,  0,-10,
                     -10,  5,  5, 10, 10,  5,  5,-10,
                     -10,  0, 10, 10, 10, 10,  0,-10,
                     -10, 10, 10, 10, 10, 10, 10,-10,
                     -10,  5,  0,  0,  0,  0,  5,-10,
                     -20,-10,-10,-10,-10,-10,-10,-20 ]
                        
MOVE_VALUE_ROOK = [0,  0,  0,  0,  0,  0,  0,  0,
                   5, 10, 10, 10, 10, 10, 10,  5,
                  -5,  0,  0,  0,  0,  0,  0, -5,
                  -5,  0,  0,  0,  0,  0,  0, -5,
                  -5,  0,  0,  0,  0,  0,  0, -5,
                  -5,  0,  0,  0,  0,  0,  0, -5,
                  -5,  0,  0,  0,  0,  0,  0, -5,
                   0,  0,  0,  5,  5,  0,  0,  0 ]  

MOVE_VALUE_QUEEN = [-20,-10,-10, -5, -5,-10,-10,-20,
                    -10,  0,  0,  0,  0,  0,  0,-10,
                    -10,  0,  5,  5,  5,  5,  0,-10,
                     -5,  0,  5,  5,  5,  5,  0, -5,
                      0,  0,  5,  5,  5,  5,  0, -5,
                    -10,  5,  5,  5,  5,  5,  0,-10,
                    -10,  0,  5,  0,  0,  0,  0,-10,
                    -20,-10,-10, -5, -5,-10,-10,-20 ]

MOVE_VALUE_KING_START = [-30,-40,-40,-50,-50,-40,-40,-30,
                         -30,-40,-40,-50,-50,-40,-40,-30,
                         -30,-40,-40,-50,-50,-40,-40,-30,
                         -30,-40,-40,-50,-50,-40,-40,-30,
                         -20,-30,-30,-40,-40,-30,-30,-20,
                         -10,-20,-20,-20,-20,-20,-20,-10,
                          20, 20,  0,  0,  0,  0, 20, 20,
                          20, 30, 10,  0,  0, 10, 30, 20 ]

MOVE_VALUE_KING_END = [-50,-40,-30,-20,-20,-30,-40,-50,
                       -30,-20,-10,  0,  0,-10,-20,-30,
                       -30,-10, 20, 30, 30, 20,-10,-30,
                       -30,-10, 30, 40, 40, 30,-10,-30,
                       -30,-10, 30, 40, 40, 30,-10,-30,
                       -30,-10, 20, 30, 30, 20,-10,-30,
                       -30,-30,  0,  0,  0,  0,-30,-30,
                       -50,-30,-30,-30,-30,-30,-30,-50 ]

square_value = [0,0,[0 for x in range(64)],
                MOVE_VALUE_PAWN,
                MOVE_VALUE_PAWN[::-1],
                MOVE_VALUE_BISHOP,
                MOVE_VALUE_BISHOP[::-1],                
                MOVE_VALUE_KNIGHT,
                MOVE_VALUE_KNIGHT[::-1],
                MOVE_VALUE_ROOK,
                MOVE_VALUE_ROOK[::-1],
                MOVE_VALUE_QUEEN,
                MOVE_VALUE_QUEEN[::-1],
                MOVE_VALUE_KING_START,
                MOVE_VALUE_KING_START[::-1]]
