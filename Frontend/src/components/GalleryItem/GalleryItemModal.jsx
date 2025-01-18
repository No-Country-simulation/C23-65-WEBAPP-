import { TransformWrapper, TransformComponent } from "react-zoom-pan-pinch";
import Modal from "@mui/material/Modal";
import PropTypes from "prop-types";

export const GalleryItemModal = ({ open, onClose }) => {
  return (
    <Modal
      open={open}
      onClose={onClose}
      className="flex flex-col items-center justify-center gap-4"
    >
      <div className="p-0 rounded-lg shadow-md w-[60vw] h-auto flex flex-col border-none">
        <TransformWrapper limitToBounds={false}>
          <TransformComponent>
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
              alt="noche"
              className="w-[60vw] object-contain"
            />
          </TransformComponent>
        </TransformWrapper>
      </div>
    </Modal>
  );
};
GalleryItemModal.propTypes = {
  open: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
};
