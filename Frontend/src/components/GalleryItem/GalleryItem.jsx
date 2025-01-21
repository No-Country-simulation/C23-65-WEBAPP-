import PropTypes from "prop-types";

export const GalleryItem = ({
  onOpen,
  selectImageToZoom,
  name,
  imageURL,
  author,
  dimensions,
  medium,
  style,
  genre,
  description,
}) => {
  return (
    <div className="w-full flex flex-col">
      <div className="w-full flex justify-center">
        <img
          // src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
          src={imageURL}
          alt={name}
          className="w-4/5 object-contain max-h-[50rem]"
          onClick={() => {
            onOpen();
            selectImageToZoom(imageURL);
          }}
        />
      </div>

      <h2 className="text-text-secondary text-xl font-semibold ml-14 my-4">
        {name}
      </h2>
      <div className="flex flex-row justify-evenly mb-6 text-text-secondary">
        <div className="w-2/5">
          <p>Autor: {author} </p>
          <p>Medidas: {dimensions} </p>
          <p>Medio: {medium} </p>
          <p>Estilo: {style} </p>
          <p>Género: {genre} </p>
        </div>
        <div className="w-2/5">
          <p>{description}</p>
        </div>
      </div>
    </div>
  );
};
GalleryItem.propTypes = {
  onOpen: PropTypes.func.isRequired,
  selectImageToZoom: PropTypes.func.isRequired,
  name: PropTypes.string.isRequired,
  imageURL: PropTypes.string.isRequired,
  author: PropTypes.string.isRequired,
  dimensions: PropTypes.string.isRequired,
  medium: PropTypes.string.isRequired,
  style: PropTypes.string.isRequired,
  genre: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
};
