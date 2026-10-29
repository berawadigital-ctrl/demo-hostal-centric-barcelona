# Contenido de la demo Hostal Cèntric (Barcelona) (es/ca/en/fr). Hechos de hostalcentric.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
# Contenido inyectado ajeno en la web del negocio (ver evidencia externa en demos/hostal-centric-barcelona/spam/spam.md): NO se usa, ni textos ni enlaces.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Individual','Doble y Twin','Triple y Cuádruple'],'ca':['Individual','Doble i Twin','Triple i Quàdruple'],'en':['Single','Double and Twin','Triple and Quadruple'],'fr':['Simple','Double et Twin','Triple et Quadruple']}
RD={
'es':['Dormitorio privado con baño para una persona.','Doble matrimonial («si os gusta dormir juntos»), doble con 2 camas y Twin Superior «para parejas o colegas exigentes».','Triple «ideal para familias o pequeños grupos», Triple Superior y Cuádruple «perfecta para familias, dos parejas o grupos de amigos».'],
'ca':['Dormitori privat amb bany per a una persona.','Doble matrimonial, doble amb 2 llits i Twin Superior, per a parelles o col·legues exigents.','Triple, ideal per a famílies o grups petits; Triple Superior i Quàdruple, per a famílies, dues parelles o grups d\'amics.'],
'en':['Private bedroom with bathroom for one person.','Double (one bed), double with 2 beds and Twin Superior, for demanding couples or colleagues.','Triple, ideal for families or small groups; Triple Superior and Quadruple, for families, two couples or groups of friends.'],
'fr':['Chambre privée avec salle de bain pour une personne.','Double (grand lit), double à 2 lits et Twin Supérieure, pour couples ou collègues exigeants.','Triple, idéale pour familles ou petits groupes ; Triple Supérieure et Quadruple, pour familles, deux couples ou groupes d\'amis.']}
ART={
'hero':('skyline',4101,['#f1ece2','#f6dcae','#f0b873','#d6926a','#5d5560','#2b3138']),
'intro':('arches',4102,['#f4eee4','#f8f4ee','#b0925f','#8a6d3b','#2b3138']),
'r1':('columns',4111,['#f3eee6','#f8f4ee','#b0925f','#8a6d3b','#2b3138']),
'r2':('arches',4112,['#f2ebe0','#e6d6b8','#c3a470','#8a6d3b','#2b3138']),
'r3':('hills',4113,['#e8ecdc','#f2e8c8','#f1cf93','#a9be9e','#7f9c84','#566f63']),
'g1':('skyline',4121,['#38343c','#e29a63','#f6d6a1','#35323a','#2a272f','#1c1a20']),
'g2':('arches',4122,['#f1e9dc','#e2cfae','#bf9f6b','#8a6d3b','#2b3138']),
'g3':('hills',4123,['#e5ead6','#f1e6c4','#f3cf8f','#a2bd98','#739a7b','#4f7059']),
'g4':('columns',4124,['#f2ece2','#f7f2ea','#b79a66','#86693a','#2b3138']),
'g5':('skyline',4125,['#3c383f','#e0a566','#f5d8a6','#39353d','#2d2931','#1d1b21']),
'g6':('arches',4126,['#f0e8da','#dfcba9','#bb9b66','#8a6d3b','#2b3138'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Cèntric · Hostal acogedor en el Eixample de Barcelona, a 400 m de la Plaza de la Universidad',see_rooms='Ver habitaciones',hero_k='Barcelona · Eixample',hero_t='Tranquilo y acogedor, en pleno Eixample',hero_s='Un hostal en un edificio clásico completamente reformado, a 400 m de la Plaza de la Universidad y a unos 10 minutos a pie de las Ramblas.',
 intro_t='Siéntete como en casa',intro_p1='El Hostal Cèntric es un establecimiento tranquilo y acogedor en un edificio clásico del Eixample completamente reformado. Sus habitaciones tienen un estilo atemporal y cálido.',
 intro_p2='Todas tienen baño privado, aire acondicionado, calefacción, TV de pantalla plana y caja fuerte; la mayoría, balcón. Hay una amplia terraza de uso público y recepción abierta las 24 horas.',
 stats=['Recepción 24 h','Eixample','Baño privado en todas','Terraza pública'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Siete tipos de habitación, de la individual a la cuádruple.',
 svcs=['Recepción 24 h','Baño privado','Aire acondicionado y calefacción','TV de pantalla plana','Caja fuerte','Balcón en la mayoría','Terraza de uso público','Personal multilingüe'],
 loc_p='Carrer de Casanova, 13 · 08011 Barcelona, a 400 m de la Plaza de la Universidad y a unos 10 minutos a pie de las Ramblas.',
 chips=['¿Qué habitaciones tiene?','¿Hay recepción 24 h?','¿Cómo llego desde el aeropuerto?','¿Cómo se reserva?']),
'ca':dict(title='Hostal Cèntric · Hostal acollidor a l\'Eixample de Barcelona, a 400 m de la Plaça de la Universitat',see_rooms='Veure habitacions',hero_k='Barcelona · Eixample',hero_t='Tranquil i acollidor, en ple Eixample',hero_s='Un hostal en un edifici clàssic completament reformat, a 400 m de la Plaça de la Universitat i a uns 10 minuts a peu de les Rambles.',
 intro_t='Sent-te com a casa',intro_p1='L\'Hostal Cèntric és un establiment tranquil i acollidor en un edifici clàssic de l\'Eixample completament reformat. Les habitacions tenen un estil atemporal i càlid.',
 intro_p2='Totes tenen bany privat, aire condicionat, calefacció, TV de pantalla plana i caixa forta; la majoria, balcó. Hi ha una àmplia terrassa d\'ús públic i recepció oberta les 24 hores.',
 stats=['Recepció 24 h','Eixample','Bany privat a totes','Terrassa pública'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Set tipus d\'habitació, de la individual a la quàdruple.',
 svcs=['Recepció 24 h','Bany privat','Aire condicionat i calefacció','TV de pantalla plana','Caixa forta','Balcó a la majoria','Terrassa d\'ús públic','Personal multilingüe'],
 loc_p='Carrer de Casanova, 13 · 08011 Barcelona, a 400 m de la Plaça de la Universitat i a uns 10 minuts a peu de les Rambles.',
 chips=['Quines habitacions té?','Hi ha recepció 24 h?','Com arribo des de l\'aeroport?','Com es reserva?']),
'en':dict(title='Hostal Cèntric · Welcoming hostal in Barcelona\'s Eixample, 400 m from Plaça de la Universitat',see_rooms='See the rooms',hero_k='Barcelona · Eixample',hero_t='Quiet and welcoming, in the heart of the Eixample',hero_s='A hostal in a fully refurbished classic building, 400 m from Plaça de la Universitat and about a 10-minute walk from Las Ramblas.',
 intro_t='Feel at home',intro_p1='Hostal Cèntric is a quiet, welcoming place in a fully refurbished classic Eixample building. Its rooms have a timeless, warm style.',
 intro_p2='All have a private bathroom, air conditioning, heating, a flat-screen TV and a safe; most have a balcony. There is a large terrace for public use and a reception open 24 hours.',
 stats=['24 h reception','Eixample','Private bathroom in all','Public terrace'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Seven room types, from single to quadruple.',
 svcs=['24 h reception','Private bathroom','Air conditioning and heating','Flat-screen TV','Safe','Balcony in most rooms','Terrace for public use','Multilingual staff'],
 loc_p='Carrer de Casanova, 13 · 08011 Barcelona, 400 m from Plaça de la Universitat and about a 10-minute walk from Las Ramblas.',
 chips=['What rooms does it have?','Is reception open 24 h?','How do I get there from the airport?','How do I book?']),
'fr':dict(title='Hostal Cèntric · Hostal accueillant dans l\'Eixample de Barcelone, à 400 m de la Plaça de la Universitat',see_rooms='Voir les chambres',hero_k='Barcelone · Eixample',hero_t='Calme et accueillant, en plein Eixample',hero_s='Un hostal dans un immeuble classique entièrement rénové, à 400 m de la Plaça de la Universitat et à environ 10 minutes à pied des Ramblas.',
 intro_t='Sentez-vous chez vous',intro_p1='L\'Hostal Cèntric est un établissement calme et accueillant dans un immeuble classique de l\'Eixample entièrement rénové. Ses chambres ont un style intemporel et chaleureux.',
 intro_p2='Toutes ont salle de bain privée, climatisation, chauffage, TV à écran plat et coffre-fort ; la plupart ont un balcon. Il y a une grande terrasse à usage public et une réception ouverte 24 h sur 24.',
 stats=['Réception 24 h','Eixample','Salle de bain privée','Terrasse publique'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Sept types de chambre, de la simple à la quadruple.',
 svcs=['Réception 24 h','Salle de bain privée','Climatisation et chauffage','TV à écran plat','Coffre-fort','Balcon dans la plupart','Terrasse à usage public','Personnel multilingue'],
 loc_p='Carrer de Casanova, 13 · 08011 Barcelone, à 400 m de la Plaça de la Universitat et à environ 10 minutes à pied des Ramblas.',
 chips=['Quelles chambres a-t-il ?','La réception est-elle ouverte 24 h ?','Comment venir depuis l\'aéroport ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
W='https://www.hostalcentric.com/'
BOOK=dict(mode='engine',url={'es':W+'habitaciones/','ca':W+'ca/','en':W+'en/rooms/','fr':W+'fr/'})
D=dict(name='Hostal Cèntric',ac='#2b3138',ac2='#b0925f',ac2_a11y='#7a5f2e',book=BOOK,around=[],foot=FOOT,
 address='Carrer de Casanova, 13 · 08011 Barcelona',phones=['+34 934 267 573'],emails=['info@hostalcentric.com'],maps='Hostal Cèntric, Carrer de Casanova 13, Barcelona',t=T)
META=dict(repo='demo-hostal-centric-barcelona',name='Hostal Cèntric',legal_name='Casanova 13, S.L.U.',registry_ids=['REAT HB-002694'],
 url='https://www.hostalcentric.com/',domain='hostalcentric.com',municipality='Barcelona',province='Barcelona',sector='hostal en el Eixample',
 read_at='2026-10-29T10:24:00+01:00',created_at='2026-10-29T10:30:00+01:00',built_at='2026-10-29T10:30:00+01:00',audit_date='2026-10-29T07:48:00+01:00',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T06:52:44+01:00',url='https://www.google.com/maps/place/Hostal+C%C3%A8ntric/@41.3824438,2.162506,17z/data=!4m9!3m8!1s0x12a4a28af14c1075:0x2eefa0e02d39042d!5m2!4m1!1i2!8m2!3d41.3824438!4d2.162506!16s%2Fg%2F1tgzk88r?hl=es&entry=ttu&g_ep=EgoyMDI2MTAyMC4wIKXMDSoASAFQAw%3D%3D'),
 book=dict(mode='engine',url=BOOK['url'],note='Los botones Reservar van a la pagina de habitaciones/inicio de su propia web en cada idioma, donde su boton RESERVA abre su motor Avirato (el enlace directo del motor lleva un parametro de identificacion que el control de seguridad S10 trata como posible secreto). La demo no construye ningun motor.'),
 first_of_type='no aplica: hostal con precedente en demos anteriores',
 nota_contenido_ajeno='La web del negocio tiene contenido inyectado ajeno oculto; la demo no usa ni enlaza nada de eso. Evidencia fuera del repo: demos/hostal-centric-barcelona/spam/spam.md')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Hay recepción 24 horas?','K03'),('¿Dónde está?','K04'),('¿Cómo llego desde el aeropuerto?','K05'),('¿Hay alguna oferta o descuento?','K06'),('¿Cómo reservo?','K07'),('¿Cuál es el teléfono?','K08'),('¿Quién es el titular?','K09'),('¿Hay parking?','K10'),('¿Tienen terraza?','K11'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K07'),('¿Hay piscina?',None),('¿Admiten mascotas?',None)],
'ca':[('Quines habitacions té?','K01'),('Què tenen les habitacions?','K02'),('Hi ha recepció 24 hores?','K03'),('On és?','K04'),('Com arribo des de l\'aeroport?','K05'),('Hi ha alguna oferta o descompte?','K06'),('Com reservo?','K07'),('Quin és el telèfon?','K08'),('Qui és el titular?','K09'),('Hi ha pàrquing?','K10'),('Teniu terrassa?','K11'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K07'),('Hi ha piscina?',None),('Admeteu mascotes?',None)],
'en':[('What rooms does it have?','K01'),('What do the rooms have?','K02'),('Is there a 24-hour reception?','K03'),('Where is it?','K04'),('How do I get there from the airport?','K05'),('Is there any offer or discount?','K06'),('How do I book?','K07'),('What is the phone number?','K08'),('Who is the owner?','K09'),('Is there parking?','K10'),('Do you have a terrace?','K11'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K07'),('Is there a swimming pool?',None),('Are pets allowed?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Qu\'ont les chambres ?','K02'),('Y a-t-il une réception 24 heures ?','K03'),('Où est-ce ?','K04'),('Comment venir depuis l\'aéroport ?','K05'),('Y a-t-il une offre ou une remise ?','K06'),('Comment réserver ?','K07'),('Quel est le téléphone ?','K08'),('Qui est le titulaire ?','K09'),('Y a-t-il un parking ?','K10'),('Avez-vous une terrasse ?','K11'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K07'),('Y a-t-il une piscine ?',None),('Les animaux sont-ils admis ?',None)]}
