import { useState } from "react";
import { Carousel } from "../../components/Carousel/Carousel";
import { GalleryItem } from "../../components/GalleryItem/GalleryItem";
import { GalleryItemModal } from "../../components/GalleryItem/GalleryItemModal";

const arts = [
  {
    name: "La noche estrellada - 1820",
    imageURL:
      "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
    author: "Vicent",
    dimensions: "120cm x 120cm",
    medium: "Oleaje sobre tela",
    style: "Impresionismo",
    genre: "Paisajismo",
    description:
      "  It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, cont",
  },
  {
    name: "La perla del mercader (1884)",
    imageURL:
      "https://cdn.discordapp.com/attachments/1326200407856250913/1330317543524794390/La_perla_del_mercader.jpg?ex=6790d602&is=678f8482&hm=662aec199f128629dcafe0a7c1f49dbee77ca1f9697424739ad90218d8ab61dd&",
    author: "Alfredo Valenzuela Puelma",
    dimensions: "215 × 138",
    medium: "oleo sobre tela",
    style: "academicismo, orientalismo",
    genre: "pintura de genero, desnudo",
    description:
      "  It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, cont",
  },
  {
    name: "Lección de geografía (1883)",
    imageURL:
      "https://cdn.discordapp.com/attachments/1326200407856250913/1330317596016509010/La_leccion_de_geografia.jpg?ex=6790d60e&is=678f848e&hm=46453dfd4c1911f46242badb1b6bbbedf1efd995cf98fe5b75dd4d335948d0b2&",
    author: "Alfredo Valenzuela Puelma",
    dimensions: "82 x 111 cm",
    medium: "oleo sobre tela",
    style: "academicismo",
    genre: "pintura de genero",
    description:
      "  It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, cont",
  },
  {
    name: "Haying at Mezy (1891)",
    imageURL:
      "https://cdn.discordapp.com/attachments/1326200407856250913/1330317713851027557/haying-at-mezy.jpgLarge.jpg?ex=6790d62b&is=678f84ab&hm=dd04a7537c83a309395db37e256779663c7cb520d1ff244b57f118f8a9a4448e&",
    author: "Berthe Morisot",
    dimensions: "50,8 x 61,6 cm",
    medium: "oleo sobre lienzo",
    style: "Impresionismo",
    genre: "pintura de genero",
    description:
      "  It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, cont",
  },
  {
    name: "Tree of life",
    imageURL:
      "https://cdn.discordapp.com/attachments/1326200407856250913/1330317792641028137/Shaki_khan_palace_interier.jpg?ex=6790d63d&is=678f84bd&hm=1373e1fcb049583917005307241f049815ff98914cde14289a123dabf8d2863e&",
    author: "Usta Gambar Karabakhi",
    dimensions: "NO DATA",
    medium: "Tempera",
    style: "ornamentalismo, muralismo",
    genre: "pintura decorativa, pintura religiosa",
    description:
      "  It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, cont",
  },
  {
    name: "Moonlit Dreams, (1874)",
    imageURL:
      "https://cdn.discordapp.com/attachments/1326200407856250913/1330317838078050456/tumblr_3ddbc3df829d80729824d3ac4739940e_dc79f556_500.jpg?ex=6790d648&is=678f84c8&hm=eb78d1b81c325cf527fe9b833f925a57e716ef41e8f448860bf13d18b02193fc&",
    author: "Gabriel Ferrier",
    dimensions: "NO DATA",
    medium: "Oleo sobre tela (presuntamente)",
    style: "Academicismo, Romanticismo",
    genre: "Pintura simbolica",
    description:
      "  It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, cont",
  },
];

export const Gallery = () => {
  const [open, setOpen] = useState(false);
  const [selectedImage, setSelectedImage] = useState("");

  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const test = arts.map((data, index) => (
    <GalleryItem
      key={index}
      onOpen={handleOpen}
      {...data}
      selectImageToZoom={setSelectedImage}
    />
  ));

  return (
    <div className="w-full flex flex-col items-center pb-10">
      <h1 className="text-2xl text-text-secondary font-bold my-6">
        Galería Nacional de PAIS - I Bimestre 2025
      </h1>
      <div className="w-4/5 flex justify-center">
        <Carousel elements={test} gallery={true} isModalOpen={open} />
      </div>

      <GalleryItemModal
        open={open}
        onClose={handleClose}
        imageURL={selectedImage}
      />
    </div>
  );
};
