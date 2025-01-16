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
      <div className="bg-background-page p-6 rounded-lg shadow-md w-[60vw] h-auto flex flex-col border-none">
        <TransformWrapper>
          <TransformComponent>
            <img
              src="https://media.admagazine.com/photos/618a7dbc58ac69e38abb6c2c/16:9/w_1280,c_limit/43884.jpg"
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
