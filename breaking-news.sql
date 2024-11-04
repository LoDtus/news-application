drop database if exists breakingnews;
create database if not exists breakingnews;
use breakingnews;

create table if not exists posts (
	id int primary key auto_increment,
    title text not null,
    thumbnail text not null,
    content longtext not null,
    creation_date datetime not null,
    is_show int not null
);

insert into posts(title, thumbnail, content, creation_date, is_show) values
('Adobe tiết lộ những địa điểm truyền cảm hứng nhất thế giới cho người làm sáng tạo',
'https://rgb.vn/wp-content/uploads/2023/11/media_18b54bbe2e495eb12be40d6859f06aa8d216e62ca.png.webp-1600x1066.jpg.webp',
'Adobe khuyên những người làm sáng tạo nên chuẩn bị cho chuyến đi của mình bằng cách lên một mood board về thành phố mà bạn đang định ghé thăm để có thể nắm bắt được bản chất của điểm đến thông qua cảnh vật, âm thanh và trải nghiệm.
“Hãy hình dung loại cảm hứng mà bạn đang tìm kiếm và những nơi bạn có thể tìm thấy nó, chẳng hạn như nhà hàng, điểm du lịch, bảo tàng hay các hoạt động”, Adobe gợi ý. 
Bạn cũng có thể ghi lại trải nghiệm của mình bằng cách quay video trong suốt hành trình. Nhật ký trực quan này có thể là nguồn cảm hứng cho bạn ngay cả sau khi chuyến đi kết thúc.
Những nghiên cứu này của Adobe cho thấy tầm quan trọng của môi trường và lối sống trong việc thúc đẩy sự sáng tạo. Nếu bạn đang gặp khó khăn trong việc tìm lại ngọn lửa đam mê, thì giờ đây bạn biết phải làm gì rồi đó!',
'2024-08-18 10:00:00', 1),
('UNIQLO ra mắt bộ sưu tập Kaws x Andy Warhol: sự kết hợp mang tính biểu tượng tôn vinh nghệ thuật đại chúng',
'https://rgb.vn/wp-content/uploads/2024/08/rgb-UNIQLO-KAWS-Andy-Warhol-UT-cv.jpg.webp',
'UNIQLO – thương hiệu thời trang Nhật Bản vừa tiết lộ sự hợp tác đưa thước đo sáng tạo lên một tầm cao mới: bộ sưu tập KAWS + Warhol UT.
Để tôn vinh sự đồng điệu của hai ngôi sao nghệ thuật đại chúng này, UNIQLO đã kết hợp các tác phẩm biểu tượng của họ với loạt sản phẩm đầy phong cách như áo thun họa tiết vui nhộn, áo khoác, tất, túi tote và một cuốn sổ nghệ thuật.
Các tác phẩm đáng chú ý bao gồm áo phông họa tiết có nhân vật BFF của KAWS nằm gần quả chuối mang tính biểu tượng của Warhol, chiếc áo khoác có hình quả chuối của Warhol ló ra khỏi túi và hình minh họa ‘Companion’ bên cạnh ‘Moon Explorer Robot’ của Warhol. 
Với mức giá từ 6 đến 70 đô la Mỹ, tất cả mọi người đều có thể tiếp cận những tác phẩm nghệ thuật này, là sự bổ sung hoàn hảo cho tủ quần áo của bất kỳ ai nghệ thuật.
Sự hợp tác này ra mắt đồng thời với triển lãm KAWS + Warhol, hiện đang được trưng bày tại Bảo tàng Andy Warhol ở Pittsburgh, Pennsylvania. Với tư cách là nhà tài trợ chính cho chuyến lưu diễn toàn cầu, UNIQLO đang giới thiệu mối liên hệ nổi bật giữa các tác phẩm biểu tượng của hai nhà tiên phong này. Triển lãm của hai thiên tài sáng tạo KAWS và Warhol diễn ra tại Pittsburgh cho đến ngày 20 tháng 1 năm 2025, trước khi bắt đầu chuyến lưu diễn quốc tế và Tokyo là điểm dừng chân cuối cùng vào năm 2026.',
'2024-08-18 10:00:00', 1),
('Những bông hoa hướng dương của Van Gogh: Chuyện chưa ai biết',
'https://rgb.vn/wp-content/uploads/2022/11/Thumbnail-Van-Gogh.png.webp',
'Một trong những tác phẩm nổi tiếng nhất của danh họa người Hà Lan  thựa ra là một bức họa trong loạt tranh hoa hướng dương của ông. Trong bài viết này, tác giả Alastair Sooke sẽ kể cho chúng ta nghe về sự ra đời những kiệt tác này.

Đôi khi, danh tiếng chói lọi có thể làm lu mờ bối cảnh và ý nghĩa ban đầu của một tác phẩm nghệ thuật. Đó cũng chính là trường hợp của bộ tranh Những bông hướng dương (Sunflowers), chấp bút bởi danh họa Vincent van Gogh.
Hãy ngắm nhìn bức tranh đang được treo tại Phòng trưng bày Quốc gia của London mà danh họa người Hà Lan đã vẽ ở Arles, miền Nam nước Pháp vào tháng 8 năm 1888. Mười lăm bông hoa hướng dương được cắm trong một chiếc bình đất nung đơn điệu trên nền màu vàng rực. Một số bông hoa vẫn tươi tắn nở bung, tựa như vòng lửa lấp lánh, với những cánh hoa vàng tỏa rực bao tròn lấy nhụy. Nhưng bên cạnh đó lại là những bông hoa đã kết hạt và bắt đầu tàn rũ .

Vừa mang thông điệp tinh thần về sự thay đổi của thời gian, bức tranh vừa mang đến một sự thay đổi đầy màu sắc, đối lập mạnh mẽ với truyền thống cũ kỹ của hội họa hoa Hà Lan thời bấy giờ, vốn đã kéo dài từ thế kỷ 17. Kể từ khi được đưa vào bộ sưu tập của Phòng trưng bày Quốc gia vào năm 1924, bức tranh đã trở nên nổi tiếng đến khó tin. Năm 2013, đã có rất nhiều bưu thiếp in hình bức tranh này được bán tại quầy lưu niệm của Phòng trưng bày – con số chính xác là 26.110 chiếc – nhiều hơn bất kỳ bức tranh nào khác trong toàn bộ bộ sưu tập.',
'2024-08-18 10:00:00', 1),
('Phân tích chiến dịch re-brand và thiết kế bộ nhận diện thương hiệu mới của Vinamilk',
'https://rgb.vn/wp-content/uploads/2023/07/358688708_9610943032310783_2933622226499926859_n-1600x895.jpg.webp',
'Logo và bộ nhận diện thương hiệu mới của Vinamilk trở thành một chủ đề hot được cộng đồng các nhà thiết kế và quảng cáo quan tâm. Cùng phân tích chiến lược thương hiệu cũng như bộ nhận diện mới của Vinamilk qua bài viết của Phan Nhật Minh – Branding Researcher & Founder của TDC – The Design Council.
Logo Vinamilk được cập nhật từ dạng phù hiệu (emblem) sang dạng biểu tượng chữ (wordmark). Theo giải thích từ đại diện hãng, chữ “Vinamilk” được viết nét tay, tổng thể logo “đơn giản mà táo bạo”. Ẩn trong logo mới là nét cười (ở chữ “i”) và hình ảnh giọt sữa ở phần bụng chữ “a”, dưới chân biểu trưng mới là chữ “Est 1976” viết tách rời nhau. Tất cả phần chữ được thể hiện bằng màu trắng, sử dụng nền xanh tím (màu xanh lam pha sắc đỏ) khá tối.',
'2024-08-18 10:00:00', 0),
('Dự án minh họa vector những MV nổi bật đánh dấu sự nghiệp 10 năm hoạt động của Kawaii Tuấn Anh',
'https://rgb.vn/wp-content/uploads/2022/11/Cover.png.webp',
'Cơ duyên thông qua dự án này, Thiện kể về lần tham gia cuộc thi làm phim ngắn 5 MINUTES SHORT FILM FESTIVAL tại trường đại học FPT – nơi mà Thiện đang theo học, “Hôm đó, Anh Kawaii là một trong những giám khảo trong cuộc thi. Sau đêm chung kết, mình may mắn kết nối với anh Kawaii và ekip phim của mình một buổi cà phê. Mình nhận được ngỏ lời về dự án vẽ minh họa này,” Anh chàng nhớ lại.

Ngay sau đó, Thiện kết hợp với Duy Torao cùng nhau bắt tay vào quá trình sáng tạo dự án, ý tưởng xuất phát từ một đồ án cách điệu chân dung của Thiện tại trường, cũng là bức poster Kẻ cắp gặp bà già – Hoàng Thuỳ Linh trong dự án. Kawaii Tuấn Anh khá thích thú và chủ động đề xuất thực hiện về bộ minh họa.

Thiện bộc bạch: “Mình cùng anh Duy có những thử nghiệm sáng tạo trong từng bức vẽ. Sau đó, nhận được phản hồi mang tính xây dựng từ anh Kawaii giúp tụi mình học hỏi nhiều hơn. Đôi lúc mình còn nhận được những lời nói vui vẻ từ anh Kawaii như ‘anh tin vào sự sáng tạo của team em’, ‘team em cứ triển đi’..”',
'2024-08-18 10:00:00', 1),
('Đắc Trung: “Có bao giờ bạn đã vẽ ra những căng thẳng chưa?”',
'https://rgb.vn/wp-content/uploads/2022/09/Cover_DacTrung.png.webp',
'Trần Đắc Trung – Họa sĩ minh họa
Trung có thổ lộ với tôi thêm: “Hết cấp ba mình đi du học ở Singapore, ngành Quản trị kinh doanh. Do từ bé thích vẽ bậy nên lúc học đại học mình vẫn tiếp tục vẽ, tới năm ba đại học thì bắt đầu vẽ lặt vặt như vẽ thiệp cưới, tranh nho nhỏ, mình hay nhận để trang trải tiền trong lúc đi học.

Lúc đi làm mình làm đúng ngành học, nên công việc cũng không liên quan gì đến vẽ, nhưng mình vẫn hay nhận công việc vẽ và tham gia các cuộc thi minh họa để theo đuổi đam mê. Thời gian biểu chủ yếu đi làm tầm 8-9h về thì vẽ, hoặc vẽ lúc cuối tuần mình vẫn duy trì tới bây giờ.” ',
'2024-08-18 10:00:00', 0),
('100 Thức Ngon Sài Gòn qua nét vẽ sống động của nghệ sỹ Daniel Tingcungco',
'https://rgb.vn/wp-content/uploads/2022/06/rgb-creative-art-Daniel-Tingcungco-100-thuc-ngon-saigon.jpg.webp',
'Sau loạt tranh vẽ 100 Góc Phố Sài Gòn vô cùng thành công ra mắt vào năm ngoái khi thành phố vẫn còn đang chìm trong đại dịch, nghệ sỹ đến từ Philippines Daniel Tingcungco nay đã tái xuất với một dự án về Sài Gòn khác cũng độc đáo và vô cùng đẹp mắt không kém có tên 100 Thức Ngon Sài Gòn. Trong series lần này, Daniel chọn chủ thể là những món ăn vô cùng đặc trưng và phổ biến ở Sài Gòn và biến chúng thành những tác phẩm nghệ thuật thật sự, qua đó thể hiện tình yêu của anh đối với nơi đây.

RGB rất vui khi một lần nữa được Daniel chọn làm nơi đầu tiên chia sẻ dự án này đến công chúng. Hãy cùng chúng tôi nghe anh ấy chia sẻ về dự án đầy thú vị này nhé!',
'2024-08-18 10:00:00', 0),
('NGOẶM: Hòa quyện bản sắc văn hóa độc đáo trong thiết kế thương hiệu ẩm thực Việt từ Studio Cohe',
'https://rgb.vn/wp-content/uploads/2021/07/51ecd8123382781.60ed79baa89e7.jpg.webp',
'Ngoặm được xem như điểm dừng chân cho việc giao lưu của đa văn hóa, là nơi hội tụ ẩm thực từ khắp mọi miền đất nước, đến gặp mặt, trò chuyện và giao lưu. Ở Ngoặm, mỗi món ăn đem đến một concept độc đáo và được thể hiện theo phong cách riêng.

Ngoặm với hình thức bài trí theo phong cách bistro được thiết kế trực quan, mang đậm nét nổi bật riêng biệt và tái cấu trúc lại brand story thành một câu chuyện cô đọng và gắn kết nhằm làm nổi bật sự đa dạng của nhiều nền văn hóa. ‘

Về font chữ, Ngoặm sử dụng các ký tự kiểu chữ ransom độc đáo, vui nhộn để làm chủ đạo, đem đến một diện mạo mới thực sự tạo ấn tượng về nơi dành cho việc trải nghiệm văn hóa ẩm thực: mà tại nơi đó mọi sự đa dạng trở nên thống nhất, nơi mà không khí văn hóa được lan tỏa thổi hồn sức sống vào trong từng hương vị món ăn.',
'2024-08-18 10:00:00', 1),
('Gaieté – hơi thở thiên nhiên với những gam màu tinh tế trong bộ branding design từ M – N Associates',
'https://rgb.vn/wp-content/uploads/2021/05/rgb-gaiete-branding-design.jpg.webp',
'Sản phẩm thời trang của Gaieté trung thành với những hoạ tiết hoa lá maximal, được sản xuất với chất lượng cao và gia công đường may tỉ mỉ, tạo sự thoải mái cho những người yêu thiên nhiên. Tập trung chủ yếu vào mua sắm trực tuyến để tạo ra trải nghiệm khác biệt, chúng tôi đã biến gói bưu phẩm giao đến khách hàng thành một chiếc hộp bí ẩn tuyệt vời làm bằng chất liệu sang trọng, canh tranh giữa thị trường với đầy những hộp carton và băng keo.
Bằng cách này, công đoạn unboxing trở nên đặc biệt và đáng nhớ hơn. Để tiếp tục phát triển câu chuyện thương hiệu, logo của nhãn hàng là một thiết kế chữ cách điệu theo lối viết tay, đại diện cho nét tinh tế và thanh lịch của sản phẩm, được truyền cảm hứng từ chính tinh thần người sáng lập.
Thông điệp văn phong cùng với phông chữ Wulkan Display dùng để truyền đạt triết lý của thương hiệu xuất hiện từ các ấn phẩm in ấn như danh thiếp, tờ bướm, bao bì cho đến các kênh truyền thông số như trang web, mạng xã hội. Tất cả đã tạo thành những mảnh ghép đầy sự vui tươi, nhiệt huyết và cá tính trải dài khắp các kênh quảng bá của nhãn hàng.',
'2024-08-18 10:00:00', 1),
('KSOUL – Bộ Branding studio Kiến trúc, nội thất ấn tượng từ M – N Associates',
'https://rgb.vn/wp-content/uploads/2020/12/rgb-creative-branding-design-mn-associate-ksoul.jpg',
'Từng được biết đến với bộ Branding Guta Cafe, M — N Associates là một studio thiết kế trẻ nhưng gây ấn tượng mạnh với những sản phẩm sáng tạo chất lượng. Bộ Branding KSOUL – một studio về Kiến trúc, nội thất tiếp tục là một project ấn tượng khác từ đội ngũ M – N Associates.
Giới thiệu về KSOUL: Được ủy thác thiết kế hơn 500 dự án từ khu dân cư đến những cửa hàng bán lẻ và chuỗi ẩm thực nổi tiếng tại Việt Nam, KSOUL Studio là công ty kiến ​​trúc & nội thất mới nổi do Huỳnh Thế Nguyễn sáng lập và lãnh đạo. KSOUL đóng một vai trò quan trọng trong việc định hình lại các con phố mua sắm của Việt Nam hiện đại, khiến chúng trở nên nhộn nhịp và đông đúc hơn với các công ty khởi nghiệp dành cho giới trẻ.
Sức hấp dẫn của concept này bắt đầu từ chữ cái K trong Ksoul, viết tắt của từ kinetic. M — N Associates team đã tạo ra một hệ thống có khả năng lặp lại sự linh hoạt của việc bố trí nội thất và lấy cảm hứng từ các hình dạng hình học của bản vẽ. Hệ thống này tỏ ra cực kỳ thú vị và phản hồi nhanh chóng trên các ứng dụng, trong khi vẫn duy trì được sự tối giản. Áp dụng hệ thống này vào chữ cái K, nó đã biến logo của KSOUL Studio thành một biểu tượng năng động và hiện đại, không còn là một biểu tượng cứng nhắc nữa.',
'2024-08-18 10:00:00', 1),
('Loạt tác phẩm tri ân & tưởng nhớ huyền thoại Akira Toriyama – cha đẻ ‘7 Viên Ngọc Rồng’ qua đời ở tuổi 68',
'https://rgb.vn/wp-content/uploads/2024/03/Akira-Toriyama-tac-gia-7-vien-ngoc-rong-qua-doi-rgb-ftt.jpg.webp',
'Là tuổi thơ của biết bao thế hệ, là thần tượng của hàng triệu người yêu thích truyện tranh và truyền cảm hứng cho rất nhiều nghệ sĩ, nhà thiết kế trên toàn thế giới – Akira Toriyama, cha đẻ bộ truyện “7 viên ngọc rồng” đã qua đời ở tuổi 68.

Vào ngày 1/3/2024, người hoạ sĩ Nhật Bản tài năng, cha đẻ của bộ truyện huyền thoại Dragon Ball đã mãi mãi ra đi để lại sự nuối tiếc cho hàng triệu người hâm mộ. Để tri ân và tưởng nhớ một tài năng đã làm nên tuổi thơ của nhiều thế hệ, người hâm mộ trên khắp thế giới đã tạo ra những tác phẩm tri ân hoạ sĩ Akira Toriyama.',
'2024-08-18 10:00:00', 1),
('Thiết kế đồng phục Olympics 2024 của Mông Cổ gây ấn tượng trên “sàn runway” thế vận hội Paris',
'https://rgb.vn/wp-content/uploads/2024/07/rgb-olympics-paris-mongolia-michel-amazonka-cv.jpeg.webp',
'Trong kỳ Olympics Paris 2024, ngoài các môn thể thao thì trang phục thi đấu và nghi lễ của các quốc gia đã thu hút sự chú ý toàn cầu. Và Mông Cổ, quốc gia nổi tiếng với di sản văn hóa phong phú, đã trình làng những bộ đồng phục được xem là kiệt tác.
Được thiết kế bởi thương hiệu thời trang Michel&Amazonka, đồng phục Olympics 2024 của Mông Cổ là sự pha trộn giữa truyền thống và hiện đại. Những bộ trang phục cầu kỳ thể hiện nổi bật về tay nghề thủ công của ba chị em – Michel, Amazonka và Munkhjargal Choigaalaa – những người điều hành thương hiệu.
Đồng phục được khen ngợi vì vẻ đẹp và yếu tố truyền thống được kết hợp tài tình với yếu tố hiện đại. Cư dân mạng khen ngợi Mông Cổ vì đã bật đèn xanh cho những bộ trang phục đẹp mắt cho vận động viên của họ. Trang phục này thậm chí còn lọt vào mắt xanh của cựu biểu tượng điền kinh người Mỹ, Michael Johnson, người tin rằng Đội Mông Cổ xứng đáng nhận “huy chương vàng trên sàn runway” Olympics Paris 2024 vì trang phục tuyệt vời đó.',
'2024-08-18 10:00:00', 1),
('Bon Trend: Muộn rồi sao mà còn ‘Ủa em!!’ – cuộc sống agency là thế này đây',
'https://rgb.vn/wp-content/uploads/2021/05/RGB-creative-bon-trend-agencylife.jpg.webp',
'Đã là người chơi hệ agency thì không thể không quen thuộc với hai từ “Ủa em!!” đa nghĩa, đầy cảm thán. Cùng Bon Trend xem qua bộ ảnh “hề hước” về câu nói “ám ảnh này”!

“Ủa em!!” – câu nói thân thương khiến dân “Ngành” giật mình tột độ mỗi khi nghe thấy. Bởi vì “Ủa em!!” có thể là feedback lúc giữa khuya, một task mới vào ngày nghỉ, hay cũng có thể là báo hiệu job chưa thể xong dù mới được khen “ờ mây zing, done nhé”.
Có nhiều nghĩa có thể được dịch ra từ hai từ “Ủa em!!”, có thể gây hoang mang nhưng cũng vô cùng đáng yêu mỗi khi nhắc đến Client. Cùng xem bộ ảnh vui với sự kết hợp của “Ủa em!!” vào các bài hát Vpop nổi tiếng.
',
'2024-08-18 10:00:00', 0),
('10 xu hướng thiết kế nhà ở cho năm 2024',
'https://rgb.vn/wp-content/uploads/2024/01/home-predictions-GettyImages-1464461010-e324e930ee1e4503a2cfba6453c23810.jpg',
'Năm mới đã đến với những xu hướng thiết kế nhà ở mới. Vậy những xu hướng nào đã trở nên lỗi thời và những gì sẽ trở thành mốt? Hãy cùng tham khảo một số xu hướng nhà ở được các chuyên gia thiết kế và kiến trúc sư nội thất nổi tiếng dự đoán cho năm 2024 dưới đây nhé. Từ đồ nội thất cho đến màu sơn và nhiều hơn thế nữa, hy vọng chúng sẽ giúp bạn định hình được phong cách mới đầy hấp dẫn cho ngôi nhà của mình.

Năm mới đã đến với những xu hướng thiết kế nhà ở mới. Vậy những xu hướng nào đã trở nên lỗi thời và những gì sẽ trở thành mốt? Hãy cùng tham khảo một số xu hướng nhà ở được các chuyên gia thiết kế và kiến trúc sư nội thất nổi tiếng dự đoán cho năm 2024 dưới đây nhé. Từ đồ nội thất cho đến màu sơn và nhiều hơn thế nữa, hy vọng chúng sẽ giúp bạn định hình được phong cách mới đầy hấp dẫn cho ngôi nhà của mình.

10 xu hướng thiết kế nhà ở cho năm 2024:
Đường cong
Các không gian lấy cảm hứng từ phòng trưng bày nghệ thuật
Kim loại hỗn hợp
Sự cộng tác của các nhà thiết kế nổi tiếng và nhiều thương hiệu đại chúng
Màu tím đậm lên ngôi
Giảm chất thải
Các tông màu đất
Phòng tắm như ở spa
Đưa không gian ngoài trời vào nhà
Những điểm nhấn táo bạo
Đường cong

Thiết kế của Maestri Studio / Ảnh: Jenifer McNeil Baker
Đồ nội thất dài, vuông vắn dường như đã đạt đến đỉnh điểm vào năm 2023. Sang năm 2024, đường cong sẽ được ưa chuộng hơn. Ghế sofa, bàn ăn hay bàn cà phê sẽ phát huy năng lượng mềm mại, êm đềm tạo nên không gian thân thiện khi được thiết kế với đường cong.

“Các đường cong mang tính sinh học và gần gũi với thiên nhiên hơn. Thế giới tự nhiên tạo ra những hình dạng hữu cơ tốt nhất, vì vậy cũng thật hợp lý khi chúng ta mang nguồn cảm hứng đó vào ngôi nhà của mình”, nhà thiết kế nội thất và chuyên gia nhà ở Joshua Smith, chia sẻ.
Nhà thiết kế nội thất Carmeon Hamilton, dẫn chương trình Reno My Rental của HGTV, bày tỏ quan điểm rằng những không gian cực kỳ hiện đại mang đậm tính nghệ thuật sẽ tạo nên trào lưu vào năm 2024. Những màu sắc táo bạo, phông nền trơn và những điểm nhấn bất ngờ, chẳng hạn như bàn cocktail vui nhộn và đèn neon có màu sắc rực rỡ, là những thứ bạn có thể tham khảo.

“Bạn có thể gọi chúng là xu hướng, nhưng đối với tôi đó là những thứ sẽ nâng tầm các thiết kế hiện tại của bạn”, Hamilton nói.',
'2024-08-18 10:00:00', 1),
('Hàn Quốc sắp xây dựng vòng đu quay không nan hoa lớn nhất thế giới',
'https://rgb.vn/wp-content/uploads/2023/03/334986178_3474009496257033_7956934764840134104_n-1600x1018.jpg.webp',
'Chính quyền thành phố Seoul (SMG) vừa tiết lộ kế hoạch xây dựng một đài quan sát hình chiếc nhẫn khổng lồ trên một bãi rác cũ. Có tên là Seoul Ring, sau khi hoàn thành nó sẽ là vòng đu quay không nan hoa lớn nhất thế giới với đường kính lên tới 180m. 

Cấu trúc này được kỳ vọng sẽ làm sống động đường chân trời của Công viên Haneul (có nghĩa là bầu trời hoặc thiên đường), vốn từng là nơi xử lý rác nhưng hiện đã được đại tu thành một công viên sinh thái.
Để phù hợp với các mục tiêu bền vững, “chiếc nhẫn” khổng lồ này sẽ chạy bằng năng lượng xanh, bao gồm cả năng lượng mặt trời. Nó sẽ chứa 36 toa xe bằng kính, với sức chứa 25 người trên mỗi toa và có thể đón tới 1.200 du khách mỗi ngày.
',
'2024-08-18 10:00:00', 0),
('[Nhân vật của tuần] Hưng Phạm: Design cũng như giải trí',
'https://rgb.vn/wp-content/uploads/2011/10/rgb.vn_hungpham.jpg',
'“Chạm ngõ” thế giới digital art từ năm 2005, được chọn tham gia trong dự án đào tạo của một công ty hoạt hình Nhật Bản, là thành viên của nhóm những người đầu tiên sáng tạo hình hiệu cho kênh Yeah1 trong thời gian đầu, sáng tạo hình ảnh cho MV Production, Focus1, SNtv, được tôn vinh tác phẩm trên 4 tạp chí thiết kế nổi tiếng: Advanced photoshop, Photoshop Creative, Photoshop User, Practical Photoshop. Hưng Phạm là một Motion Graphic Designer 24 tuổi đến từ Sài Gòn, hiện đang theo học Multimedia Graphic Design ở Bellevue College, WA. Với thế mạnh kết hợp Photoshop và Cinema4D để tạo ra những tác phẩm mang phong cách Photo Manipulation đầy ấn tượng và các sản phẩm motion graphic rất riêng.

Cùng trò chuyện với Hưng Phạm trong bài phỏng vấn đặc biệt của RGB.vn để hiểu hơn về anh và quá trình sáng tạo các tác phẩm ấn tượng của mình. Đồng hành cùng “Nhân vật của tuần” để gặp gỡ, kết nối với những designer tài năng của Việt Nam và chia sẻ mọi thứ trong lĩnh vực Multimedia.',
'2024-08-18 10:00:00', 1),
('Purple Taro Cat – “Khi sáng tạo dành cho nhiều người xem, bạn đặt ra những tiêu chí gì?',
'https://rgb.vn/wp-content/uploads/2023/11/rgb-creative-ha-phuong.jpg',
'Purple Taro Cat với những tác phẩm mang làn gió tươi mới, diễn hoạt câu chuyện đầy lôi cuốn bên trong đó. Purple Taro Cat (Mèo Khoai Tím) – tên thật của cô là Hà Phương. “Mình hiện là hoạ sĩ minh hoạ tự do ở Sài Gòn. Mình rất rất thích mèo và màu tím. Ngoài vẽ thì mình còn thích khám phá làm đồ thủ công từ resin, stone clay và plastic shrink…”.

Hà Phương bày tỏ việc thích vẽ vời và làm thủ công ngay từ bé, cô chính thức bước vào chặng đường sáng tạo khi lựa chọn ngành học Thiết kế đồ họa tại trường Đại học. Trong quá trình được thực hành nhiều mảng trong thiết kế liên quan, cô ấn tượng trước sự nghiệp vẽ minh hoạ, và cô đã theo đuổi đến tận bây giờ.
“Mình có rất nhiều trải nghiệm khác nhau với việc vẽ minh hoạ, từ đồ án tốt nghiệp mình được vẽ về đề tài Hội An. Cho tới những sản phẩm quà tặng du lịch thể hiện đặc trưng văn hoá Việt Nam. Cho tới sách Ehon thiếu nhi, vẽ áp phích cho thương hiệu thời trang, các sản phẩm in ấn như tờ rơi, banner. Tuy nhiên mình vẫn thích được vẽ và tự sản xuất những sản phẩm riêng như các bộ stickers (những tem dán), postcard (bưu thiếp), thiệp, tranh, lịch,… Mình còn từng có thời gian dạy vẽ cho thiếu nhi nên mình cũng được trải nghiệm việc vẽ các giáo án cho các bạn nhỏ. Mình còn vẽ trên các sản phẩm thủ công như đất sét, art toy (đồ chơi nghệ thuật), và cả vẽ tường. Mình cũng rất thích tham gia các cuộc thi, challenge như Inktober, hoặc các challenge hàng năm của Vietnam Local Artist…”',
'2024-08-18 10:00:00', 1),
('Mummy Brown: bột nâu rùng rợn được nghiền từ xác ướp Ai Cập, từng được dùng để vẽ nên các tác phẩm nghệ thuật nổi tiếng',
'https://rgb.vn/wp-content/uploads/2023/03/Eugene_Delacroix_-_Liberty_Leading_the_People_28th_July_1830_-_WGA6177-1.jpg.webp',
'Một trong những bức hoạ nổi tiếng nhất sử dụng loại “bột người” này đó chính là bức Liberty Leading The People (1830) của Eugène Delacroix.

Mummy Brown là tên gọi của một loại bột vẽ từng được dùng phổ biến trong giới họa sĩ châu Âu từ thế kỷ 16 nhờ đặc tính trong suốt và linh hoạt độc đáo của nó khi kết hợp với dầu và màu nước để mô tả bóng tối và tông màu da của con người. Thế nhưng, có một sự thật rùng rợn ít ai ngờ tới là nó được làm từ những xác ướp thực sự của mèo và người được nhập khẩu từ Ai Cập. Loại vật liệu rùng rợn này sau đó được nghiền thành bột để hỗ trợ cho việc tạo bóng trong các bức tranh.
Một trong những bức hoạ nổi tiếng nhất sử dụng loại “bột người” này đó chính là Liberty Leading The People (1830) của Eugène Delacroix. Trong bức tranh, Nữ thần Tự do đang dẫn dắt nhân dân đến bến bờ tự do, thế nhưng trớ trêu thay bức tranh thực sự lại chứa dấu vết của những người đã chết. ',
'2024-08-18 10:00:00', 1),
('Ziêm – Quan sát cách vận hành của thế giới để bắt đầu vào sáng tạo',
'https://rgb.vn/wp-content/uploads/2023/11/rgb-creative-ziem.jpg',
'Hoàng Minh Thu, còn được biết đến với tên Ziêm – một giáo viên dạy vẽ cho người lớn tại Trung tâm Mỹ thuật Bụi ở Hà Nội. Ngoài công việc giảng dạy, cô ấy cũng là một sinh viên chuyên ngành Thiết kế đồ họa. Đam mê nghệ thuật của Ziêm bắt đầu từ việc vẽ tranh trước khi cô ấy tiếp tục khám phá lĩnh vực thiết kế đồ họa.

Mặc dù ba cô không phải là một họa sĩ, nhưng ông đã có vai trò quan trọng trong việc hình thành hành trình nghệ thuật của Ziêm. Ông từng là một giáo viên mầm non và theo đuổi bằng cấp về Mỹ thuật để dạy cho các em nhỏ. Ziêm tin rằng niềm đam mê của mình đối với nghệ thuật và công việc giảng dạy là do sự di truyền của bộ gen nghệ sĩ từ cha mình.
Trong lĩnh vực thiết kế đồ họa, sự tò mò và khả năng quan sát sắc bén của Ziêm đã đóng vai trò quan trọng. Từ nhỏ, cô luôn thích quan sát các vật thể trong cuộc sống hàng ngày và đặt câu hỏi về mục đích của chúng. 

Khi còn nhỏ, cô thắc mắc: “Tại sao biển báo giao thông chỉ sử dụng các màu xanh, đỏ và vàng mà không có màu hồng hay cam?” Khi lớn lên, những câu hỏi của cô trở nên phức tạp hơn, như: “Nếu tôi đặt một biển báo ở vị trí A, liệu nó có dễ nhận biết hơn cho người lái xe trong vài giây ngắn ngủi không?”. Câu hỏi của Ziêm thường xoay quanh các chủ đề liên quan đến cuộc sống hàng ngày, đặc biệt là vận hành của hệ thống đường bộ và các công trình kiến trúc. 

“Mình tin rằng sự quan tâm đặc biệt đến những chủ đề như vậy của mình cũng xuất phát từ việc ba thường nhắc nhở mình về việc lái xe cẩn thận và chia sẻ những câu chuyện về những vụ tai nạn đáng tiếc.” Vì được cha mẹ cho phép đi xa một mình từ khi còn nhỏ, Ziêm cũng rất quan tâm đến những vấn đề đó. Dần dần, thiết kế trở thành một phần không thể thiếu trong nhận thức của cô, phát sinh từ thói quen quan sát đó.” Ziêm chia sẻ.',
'2024-08-18 10:00:00', 0),
('alectruha: “Mình đã phản chiếu bản thân qua những tác phẩm sáng tạo như thế này”',
'https://rgb.vn/wp-content/uploads/2023/05/rgb-creative-alectruha.jpg',
'“Bạn đã tự vấn/phản chiếu bản thân sau mỗi lần sáng tạo như thế nào?” – Câu hỏi đầu tiên dành cho khách mời cũng là chủ đề chính được đề cập trong bài viết.

Khách mời số bài viết này được nhắc đến là alectruha – một bạn thực hành vẽ minh họa sinh sống tại Thành phố Hồ Chí Minh, với những tác phẩm mang phong cách doodle hay free-hand drawing. Bằng một cách mới lạ, tác phẩm của alectruha sử dụng chất liệu màu sắc đầy thu hút, những hình tượng khá độc đáo, đôi lúc trừu tượng, khó hiểu.

alectruha tên thật là Hà Phan Minh Trụ – hiện tại, anh là người vẽ minh họa tự do. Song song đó, anh là sinh viên học ngành Tâm lý học. “Đối với mình việc thực hành nghệ thuật như một cơ chế tự bảo vệ và giải tỏa trước những khó khăn tinh thần trong cuộc sống. Ngoài ra, mình còn là một người hướng dẫn các hoạt động nghệ thuật mang tính chất chữa lành/ thư giãn. Mình nghĩ điểm mạnh của mình chính là màu sắc mình dùng trong các tác phẩm, mình nghĩ nó thoải mái, trẻ con, phóng khoáng.”  alectruha nói!',
'2024-08-18 10:00:00', 1),
('Dung Lê: “Mình thích lượm lặt những thứ nhỏ trong cuộc sống để triển khai khi vẽ”',
'https://rgb.vn/wp-content/uploads/2023/01/rgb-creative-talk-dung-le.jpg.webp',
'Tôi bắt gặp được những tác phẩm khá thú vị từ đội nhóm trên mạng xã hội, nó làm tôi thật sự đầy cảm hứng đấy chứ. Tôi thấy được câu chuyện có vẻ đời thường từ những bức tranh trong dự án. Tôi có liên hệ đến để được trò chuyện, hơn hết tôi đang khai thác một cách đầy học hỏi, mới mẻ.

Dung Lê & Những trải nghiệm tuổi thơ: “Từ nhỏ mình phụ mẹ và tiếp xúc nhiều..”
Dung Lê là người kể chuyện bằng tranh – cô ấy nói với tôi như thế. “Mình thích được gọi như vậy vì nghe có lẽ đúng về cách mà mình đang làm việc vẽ”. Ban ngày, Dung làm một công việc khác, trước đây, cô là sinh viên ngành kiến trúc trường Đại học Duy Tân. Từ nhỏ, cô thích vẽ tranh một cách linh tinh, nên bây giờ thời gian rảnh, sau giờ làm, công việc thứ 02 của Dung là vẽ minh họa.
Cô kể về những trải nghiệm tuổi thơ của mình, có vẻ gì đó thô mộc nhưng không kém đầy cảm hứng. “Mẹ mình buôn bán trong chợ, từ nhỏ mình đi phụ mẹ thì đã được tiếp xúc nhiều với các mẹ, các bà, các cô. Thế nên đa phần trong các tranh mình kể đều có dáng dấp những người phụ nữ và câu chuyện của họ.

Mình cũng hay nghe podcast (tạm dịch: âm thanh được thu sẵn và phát trên những nền tảng trực tuyến) rồi suy nghĩ vớ vẩn về những thứ mình thấy mình nghe mình cảm. Đấy đều là những chất liệu làm nên câu chuyện của mình.”

Còn về những trải nghiệm sáng tạo hiện tại thì sao, Cô trả lời với tôi đầy vẻ hào hứng, Dung nói những trải nghiệm của mình không hề sáng tạo: “Vì mình bắt đầu làm điều mình đam mê trước, việc giải phóng những suy nghĩ và năng lượng bản thân cũng góp phần tạo nên nhiều thứ hay ho và mới mẻ..”',
'2024-08-18 10:00:00', 1)
;

create table if not exists emails (
	id int primary key auto_increment,
    email text not null,
    join_date datetime not null
);

insert into emails(email, join_date) values
('nguyentrunglong.150903@gmail.com', '2024-08-18 10:00:00'),
('nguyentrunglong.15092003@gmail.com', '2024-08-19 10:00:00'),
('trunglong1592003@gmail.com', '2024-08-20 10:00:00'),
('nguyentrunglong101261592003@gmail.com', '2024-08-21 10:00:00')
;

create table if not exists messages (
	id int primary key auto_increment,
    id_post int unique,
    send_date datetime not null,
    `subject` text not null,
    content longtext not null,
    author varchar(100) not null,
	id_receiver json not null,
    foreign key (id_post) references posts(id)
);

insert into messages (id_post, send_date, `subject`, content, author, id_receiver) values
(1, '2024-08-18 10:00:00', 'New Article Published on Breaking News!',
'I hope this email finds you well.
I am pleased to inform you that a new article has just been published on our Breaking News. We encourage you to take a moment to read it and share your thoughts.
Thank you for your continued support.', 'Breaking News', '["2", "3"]'),
(2, '2024-08-18 10:00:00', 'New Article Published on Breaking News!',
'I hope this email finds you well.
I am pleased to inform you that a new article has just been published on our Breaking News. We encourage you to take a moment to read it and share your thoughts.
Thank you for your continued support.', 'Breaking News', '["2", "3"]'),
(null, '2024-08-18 10:00:00', 'Scheduled System Maintenance Notification',
'We would like to inform you that a scheduled maintenance of our system will take place on [date] from [start time] to [end time]. During this period, access to certain services may be temporarily unavailable.
We apologize for any inconvenience this may cause and appreciate your understanding. If you have any questions, please feel free to contact us.
Thank you for your cooperation.', 'Breaking News', '["2", "3"]'),
(3, '2024-08-18 10:00:00', 'New Article Published on Breaking News!',
'I hope this email finds you well.
I am pleased to inform you that a new article has just been published on our Breaking News. We encourage you to take a moment to read it and share your thoughts.
Thank you for your continued support.', 'Breaking News', '["2"]'),
(null, '2024-08-18 10:00:00', 'Scheduled System Maintenance Notification',
'We would like to inform you that a scheduled maintenance of our system will take place on [date] from [start time] to [end time]. During this period, access to certain services may be temporarily unavailable.
We apologize for any inconvenience this may cause and appreciate your understanding. If you have any questions, please feel free to contact us.
Thank you for your cooperation.', 'Breaking News', '["2"]');

create table if not exists statistic (
	id int primary key auto_increment,
    total_post int not null,
    total_post_show int not null,
    total_post_hidden int not null,
    total_email int not null
);

insert into statistic(total_post, total_post_show, total_post_hidden, total_email) values
(21, 15, 6, 4);

create table if not exists users (
	user_id varchar(50) not null primary key,
	user_password char(68) not null,
	`active` tinyint NOT NULL
);

insert into users(user_id, user_password, `active`) values
('admin', '{noop}root', 1),
('user', '{noop}', 1);

create table if not exists roles (
	`user_id` varchar(50) not null,
    `role` varchar(50) not null,
	UNIQUE KEY `authorities5_idx_1` (`user_id`,`role`),
	CONSTRAINT `authorities5_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES users (`user_id`)
);

insert into roles(user_id, `role`) values
('admin', 'ROLE_ADMIN'),
('user', 'ROLE_USER');