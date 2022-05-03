# Node 배열 구조 || {'노드 이름':[장소명,시간,[[이웃 노드1],[이웃 노드2],[이웃 노드3]]]}
# 이웃 노드 값 구조 || ['이웃 노드 이름',거리(m),고도차(m)]
NodeSongdo = {
  'gatea': [
    '연돌(임시정문)',
    10000,
    [
      [
        ['nodea',116,2]
      ]
    ]
  ],
  'gateb':[
    '서문(트스 방향)',
    10000,
    [
      [
        ['DormC',38,0],
        ['IMCH',44,0],
        ['nodej',68,0]
      ]
    ]
  ],
  'UML':[
    '언더우드기념도서관(1층 출입구)',
    10000,
    [
      [
        ['nodee',18,0]
      ]
    ]
  ],
  'Yplaza':[
    '언더우드기념도서관(지하1층), Y-plaza',
    10000,
    [
      [
        ['nodem',57,0],
        ['noden',56,0],
        ['nodes',19,0]
      ]
    ]
  ],
  'YICfield':[
    '운동장',
    10000,
    [
      [
        ['nodea',237,2],
        ['nodeb',99,0]
      ]
    ]
  ],
  'LiberA':[
    '자유관A',
    10000,
    [ 
      [ 
        ['nodel',48,0],
        ['noder',40,0]
      ]
    ]
  ],
  'LiberB':[
    '자유관B',
    10000,
    [ 
      [ 
        ['nodea',77,0],
        ['nodel',29,0]
      ]
    ]
  ],
  'Futsal':[
    '풋살장',
    10000,
    [ 
      [ 
        ['DormB',49,0],
        ['nodek',31,0],
        ['nodep',76,0]
      ]
    ]
  ],
  'WisA':[
    '지혜관A',
    10000,
    [ 
      [ 
        ['Woori',36,0],
        ['nodek',39,0]
      ]
    ]
  ],
  'WisB':[
    '지혜관B',
    10000,
    [ 
      [ 
        ['nodeg',28,0]
      ]
    ]
  ],
  'WisC':[
    '지혜관C',
    10000,
    [ 
      [ 
        ['DormD',160,0]
      ]
    ]
  ],
  'Woori':[
    '우리은행',
    10000,
    [ 
      [ 
        ['WisA',36,0],
        ['DormA',53,0],
        ['DormB',34,0]
      ]
    ]
  ],
  'DormA':[
    '송도학사A',
    10000,
    [ 
      [ 
        ['Woori',53,0],
        ['nodea',243,2]
      ]
    ]
  ],
  'DormB':[
    '송도학사B',
    10000,
    [ 
      [ 
        ['Futsal',49,0],
        ['Woori',34,0],
        ['DormC',65,0],
        ['nodej',67,0]
      ]
    ]
  ],
  'DormC':[
    '송도학사C',
    10000,
    [ 
      [ 
        ['gateb',38,0],
        ['DormB',65,0],
        ['nodej',78,0]
      ]
    ]
  ],
  'DormD':[
    '송도학사D',
    10000,
    [ 
      [ 
        ['WisC',160,0],
        ['DormG',90,0],
        ['nodec',100,0],
        ['noded',70,2]
      ]
    ]
  ],
  'DormE':[
    '송도학사E',
    10000,
    [ 
      [ 
        ['DormF',43,0],
        ['nodec',33,0]
      ]
    ]
  ],
  'DormF':[
    '송도학사F',
    10000,
    [ 
      [ 
        ['DormE',43,0]
      ]
    ]
  ],
  'DormG':[
    '송도학사G',
    10000,
    [ 
      [ 
        ['DormF',90,0]
      ]
    ]
  ],
  'VeriA':[
    '진리관A',
    10000,
    [ 
      [ 
        ['nodem',19,0],
        ['nodes',58,0]
      ]
    ]
  ],
  'VeriB':[
    '진리관B',
    10000,
    [ 
      [ 
        ['noded',50,0],
        ['nodem',50,0]
      ]
    ]
  ],
  'VeriC':[
    '진리관C',
    10000,
    [ 
      [ 
        ['nodef',27,0],
        ['noden',70,0]
      ]
    ]
  ],
  'VeriD':[
    '진리관D',
    10000,
    [ 
      [ 
        ['SLBigen',45,0],
        ['nodef',45,0]
      ]
    ]
  ],
  'SLBigen':[
    '에스엘바이젠의학연구소',
    10000,
    [
      [ 
        ['VeriD',45,0]
      ]
    ]
  ],
  'Vision':[
    '종합관',
    10000,
    [ 
      [ 
        ['noden',17,0],
        ['nodes',54,0]
      ]
    ]
  ],
  'Chapl':[
    '크리스틴채플',
    10000,
    [ 
      [ 
        ['nodei',31,0],
        ['nodeo',27,0]
      ]
    ]
  ],
  'IMCH':[
    '국제캠퍼스기념관',
    10000,
    [ 
      [ 
        ['gateb',44,0]
      ]
    ]
  ],
  'Mntnc':[
    '파워플랜트',
    10000,
    [ 
      [ 
        ['nodei',36,0]
      ]
    ]
  ],
  'Ghome':[
    '저에너지친환경실험주택',
    10000,
    [ 
      [ 
        ['nodeh',78,0]
      ]
    ]
  ],
  'posco':[
    '포스코그린빌딩',
    10000,
    [ 
      [ 
        ['nodeg',284,0]
      ]
    ]
  ],
  'nodea':[
    'a',
    10000,
    [ 
      [
        ['gatea',116,-2],
        ['YICfield',237,-2],
        ['LiberB',77,0],
        ['DormA',243,-2]
      ]
    ]
  ],
  'nodeb':[
    'b',
    10000,
    [ 
      [ 
        ['YICfield',99,0]
        ['nodec',67,0],
        ['noder',150,2]
      ]
    ]
  ],
  'nodec':[
    'c',
    10000,
    [ 
      [ 
        ['nodeb',67,0],
        ['DormE',33,0],
        ['DormD',100,0],
        ['nodem',68,2]
      ]
    ]
  ],
  'noded':[
    'd',
    10000,
    [ 
      [ 
        ['VeriB',50,0],
        ['nodee',65,0]
      ]
    ]
  ],
  'nodee':[
    'e',
    10000,
    [ 
      [
        ['UML',18,0],
        ['noded',65,0],
        ['nodef',52,0]
      ]
    ]
  ],
  'nodef':[
    'f',
    10000,
    [ 
      [ 
        ['VeriC',27,0],
        ['nodee',52,0],
        ['VeriD',45,0],
        ['nodeg',76,-2]
      ]
    ]
  ],
  'nodeg':[
    'g',
    10000,
    [ 
      [ 
        ['nodeo',35,0],
        ['nodef',76,2],
        ['posco',284,0],
        ['WisB',28,0],
        ['nodeh',59,0]
      ]
    ]
  ],
  'nodeh':[
    'h',
    10000,
    [ 
      [ 
        ['nodei',26,0],
        ['nodeg',59,0],
        ['Ghome',78,0]
      ]
    ]
  ],
  'nodei':[
    'i',
    10000,
    [ 
      [ 
        ['nodej',153,0],
        ['Chapl',31,0],
        ['nodeh',26,0],
        ['Mntnc',36,0]
      ]
    ]
  ],
  'nodej':[
    'j',
    10000,
    [ 
      [ 
        ['DormB',67,0],
        ['nodep',63,0],
        ['nodei',153,0],
        ['gateb',68,0],
        ['DormC',78,0]
      ]
    ]
  ],
  'nodek':[
    'k',
    10000,
    [ 
      [ 
        ['nodel',119,2],
        ['Futsal',31,0],
        ['WisA',39,0]
      ]
    ]
  ],
  'nodel':[
    'l',
    10000,
    [ 
      [ 
        ['LiberB',29,0],
        ['LiberA',48,0],
        ['nodek',119,-2]
      ]
    ]
  ],
  'nodem':[
    'm',
    10000,
    [ 
      [ 
        ['VeriA',19,0],
        ['nodec',68,-2],
        ['VeriB',50,0],
        ['Yplaza',57,0]
      ]
    ]
  ],
  'noden':[
    'n',
    10000,
    [ 
      [ 
        ['Vision',17,0],
        ['Yplaza',56,0],
        ['VeriC',70,0],
        ['nodeq',123,-2]
      ]
    ]
  ],
  'nodeo':[
    'o',
    10000,
    [ 
      [ 
        ['nodep',137,0],
        ['nodeg',35,0],
        ['Chapl',27,0]
      ]
    ]
  ],
  'nodep':[
    'p',
    10000,
    [ 
      [ 
        ['Futsal',76,0],
        ['nodeq',32,0],
        ['nodeo',137,0],
        ['nodej',65,0]
      ]
    ]
  ],
  'nodeq':[
    'q',
    10000,
    [ 
      [ 
        ['noder',88,2],
        ['noden',123,2],
        ['nodep',32,0]
      ]
    ]
  ],
  'noder':[
    'r',
    10000,
    [ 
      [ 
        ['LiberA',40,0],
        ['nodeb',150,-2],
        ['nodes',58,0],
        ['nodeq',88,-2]
      ]
    ]
  ],
  'nodes':[
    's',
    10000,
    [ 
      [ 
        ['noder',58,0],
        ['VeriA',58,0],
        ['Yplaza',19,0],
        ['Vision',54,0]
      ]
    ]
  ]
}