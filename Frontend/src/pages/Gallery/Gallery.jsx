import { Carousel } from "../../components/Carousel/Carousel";
import { GalleryItem } from "../../components/GalleryItem/GalleryItem";

export const Gallery = () => {
  const test = [1, 2, 3, 4].map((_, index) => <GalleryItem key={index} />);
  return (
    <div className="w-full flex flex-col items-center">
      <h1 className="text-2xl text-text-secondary font-bold my-6">
        Galería Nacional de PAIS - I Bimestre 2025
      </h1>
      <div className="w-4/5 flex justify-center ">
        <Carousel elements={test} gallery={true} />
      </div>
    </div>
  );
};
