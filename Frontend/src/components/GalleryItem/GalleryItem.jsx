import PropTypes from "prop-types";

export const GalleryItem = ({ onOpen }) => {
  return (
    <div className="w-full flex flex-col">
      <div className="w-full flex justify-center">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
          alt="noche"
          className="w-4/5 object-contain"
          onClick={onOpen} // Llamamos a onOpen desde las props
        />
      </div>

      <h2 className="text-text-secondary text-xl font-semibold ml-14 my-4">
        La noche estrellada -1820
      </h2>
      <div className="flex flex-row justify-evenly mb-6 text-text-secondary">
        <div className="w-2/5">
          <p>Autor: Vicent</p>
          <p>Medidas: 120cm x 120cm</p>
          <p>Medio: Oleaje sobre tela</p>
          <p>Estilo: Impresionismo</p>
          <p>Género: Paisajismo</p>
        </div>
        <div className="w-2/5">
          <p>
            It is a long established fact that a reader will be distracted by
            the readable content of a page when looking at its layout. The point
            of using Lorem Ipsum is that it has a more-or-less normal
            distribution of letters, as opposed to using Content here, cont
          </p>
        </div>
      </div>
    </div>
  );
};
GalleryItem.propTypes = {
  onOpen: PropTypes.func.isRequired,
};
