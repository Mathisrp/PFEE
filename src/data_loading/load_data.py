import os
import nibabel as nib

class DATALoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self) -> tuple:
        """
        loading data from db folder
        taking only nii files
            - taking flair, t2, t1(mprage), mask1, mask2
        return -> list
        """
        data = []
        for root, dirs, files in os.walk(self.data_path):
            for dir in dirs:
                if dir.startswith("training"):
                    print(f"/preprocessed/{dir}/")
                    i = 2
                    for file in os.listdir(os.path.join(root,"preprocessed", dir)):
                        


        return data
                