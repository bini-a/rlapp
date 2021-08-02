import streamlit as st
import pandas as pd
import numpy as np
def app():
    @st.cache
    # Load data
    def load_data():
        df = pd.read_csv("main_file_dataset.csv")
        return df
    df = load_data()
    st.dataframe(df)

    

        
                    
    #  # Dictionaries with indices for history searching
    # president_indices = {"York": [7072, 14590, 50164, 50170], "Craven": [2004, 2005, 9541, 10235, 11146, 11155, 11156, 11161, 11167, 11168, 11169, 11170, 11171, 11172, 11173, 11174, 11175, 11176, 11177, 11178, 11179, 11180, 11181, 11182, 11183, 11197, 11200, 14590, 15131, 19231, 20678, 20732, 21211, 25196, 27216, 48485], 
    #           "Gannaway": [6266, 6267, 6269, 16522, 41864], "Wood": [13320, 30929, 30984, 49501, 49528], 
    #           "Crowell": [127, 11387, 19234, 32886, 46573], "Kilgo": [158, 6815, 21326, 25715, 31143, 31930, 42066, 42069, 45697, 45808], 
    #           "Few": [4293, 4295, 5490, 5535, 6660, 7338, 7356, 13399, 13678, 13680, 14742, 15288, 15290, 15291, 15292, 15293, 15294, 15726, 17493, 17627, 17628, 17632, 18218, 21323, 26808, 28326, 32409, 34437, 34637, 35247, 42069, 46891, 47138, 47141], 
    #           "Flowers": [10743, 15710, 16296, 19004, 20519, 22959, 26399, 27309, 28173, 30657, 34052, 42059, 42065, 44500, 45697], 
    #         "Edens": [], "Hart": [14123], "Knight": [5490, 25741, 30171, 47829],
    #           "Sanford": [5490, 9533, 9541, 9554, 19873, 19875, 22266, 39311, 39312, 39313, 39314, 39363, 39364, 39365, 42007, 44948, 45317], 
    #           "Brodie": [], "Keohane": [], "Brodhead": [2619, 34442, 35593]}
    # name_indices = {'brown': [], 'union': [31358, 50170], 'normal': [410, 2004, 4821, 5148, 5149, 6904, 7031, 9828, 15130, 15131, 15133, 20074, 20075, 25093, 25094, 25195, 44683, 47523, 47901, 48481, 48488], 'trinity': [127, 158, 932, 949, 1950, 2004, 2726, 4207, 4294, 4855, 4859, 5861, 5864, 5955, 6085, 6659, 6815, 6917, 6918, 6921, 7684, 7685, 7687, 7688, 7698, 7700, 8356, 9180, 9645, 10235, 10741, 10906, 10920, 11155, 11156, 11158, 11161, 11164, 11197, 11199, 11200, 11731, 11822, 12078, 13261, 13302, 13303, 13317, 13671, 13674, 14005, 15133, 16211, 17237, 17238, 17239, 17306, 17967, 19231, 19295, 19298, 19384, 20729, 20731, 21237, 21765, 22038, 22129, 22147, 22150, 22158, 23045, 24107, 24513, 24523, 24837, 25004, 25621, 25748, 27216, 27397, 27816, 27836, 28173, 28657, 28659, 28828, 30321, 30375, 30376, 30480, 30706, 30943, 30945, 30947, 30951, 31012, 31013, 31015, 31016, 31017, 31018, 31019, 31247, 31977, 32804, 32886, 34437, 34637, 34654, 35029, 35460, 37321, 37405, 37500, 37748, 37801, 38323, 38324, 39272, 39480, 39481, 39702, 40312, 40454, 40468, 40616, 40644, 40703, 41457, 41590, 41594, 41642, 41914, 42030, 42061, 42065, 42066, 42069, 42408, 42531, 42532, 42919, 42927, 43242, 43348, 43352, 43354, 43616, 43619, 44460, 44474, 44507, 44696, 45276, 45662, 45663, 45693, 45696, 45697, 45808, 46887, 47503, 47523, 49746, 49750, 49751, 50170, 50219], 'duke': [59, 60, 258, 415, 509, 515, 568, 570, 571, 572, 575, 577, 596, 749, 751, 752, 800, 878, 881, 888, 1084, 1085, 1408, 1432, 1594, 1619, 1941, 1950, 2095, 2168, 2178, 2388, 2820, 2829, 3592, 3885, 3912, 4139, 4143, 4273, 4294, 4463, 4465, 4466, 4467, 4471, 4472, 4504, 4664, 4665, 4860, 5148, 5149, 5231, 5488, 5489, 5610, 5730, 6085, 6086, 6090, 6106, 6116, 6122, 6185, 6186, 6236, 6265, 6434, 6551, 6565, 6630, 6773, 6777, 6844, 6986, 6990, 7021, 7337, 7484, 7683, 7688, 7701, 7974, 8023, 8085, 8090, 8093, 8185, 8191, 8251, 8356, 9038, 9179, 9180, 9260, 9273, 9404, 9405, 9407, 9410, 9412, 9414, 9417, 9419, 9420, 9645, 9663, 10329, 10354, 10386, 10504, 10662, 10743, 10752, 10753, 11037, 11045, 11168, 11175, 11197, 11337, 11735, 11737, 11823, 12145, 12152, 12533, 12561, 12679, 13053, 13141, 13302, 13318, 13655, 13669, 13692, 13693, 13694, 13695, 13696, 13741, 13743, 13745, 13746, 13747, 13750, 13751, 13752, 13753, 13754, 13755, 13756, 13757, 13758, 13759, 13760, 13761, 13762, 13763, 13764, 13765, 13766, 13767, 13768, 13769, 13770, 13771, 13772, 13773, 13774, 13775, 13776, 13777, 13778, 13779, 13780, 13781, 13782, 13783, 13793, 13795, 13796, 13797, 13798, 13799, 13800, 13801, 13806, 13807, 13808, 13809, 14399, 14484, 14512, 14516, 14517, 14585, 14623, 14861, 14979, 14983, 15294, 15511, 15697, 15751, 15752, 15927, 15939, 16184, 16278, 16529, 16542, 16556, 16557, 16797, 16842, 16922, 17179, 17472, 17493, 17494, 17497, 17498, 17754, 17756, 18432, 18666, 18712, 18713, 18952, 19185, 19309, 19311, 19334, 19384, 19444, 19616, 19647, 19648, 19650, 19651, 19652, 19653, 19658, 19660, 19662, 19666, 19771, 19865, 19909, 19912, 19920, 20156, 20210, 20212, 20214, 20318, 20523, 20542, 20549, 20823, 21005, 21396, 21508, 21566, 21616, 21723, 21815, 21954, 22050, 22265, 22266, 22267, 22272, 22285, 22594, 22595, 22597, 22618, 22772, 22868, 22869, 22871, 22893, 22895, 22905, 22921, 22922, 22923, 22926, 22943, 23288, 23343, 23775, 23909, 24166, 24237, 24525, 24619, 24838, 25049, 25074, 25251, 25262, 25263, 25264, 25665, 26306, 26307, 26393, 26398, 26399, 26603, 26801, 26854, 27338, 27340, 27457, 27486, 27719, 27720, 27790, 27802, 27889, 28247, 28561, 28601, 28658, 28718, 28828, 29203, 29456, 29573, 29623, 30375, 30376, 30650, 30666, 30677, 31230, 31322, 31509, 31813, 31892, 31899, 32183, 32297, 32343, 32851, 32877, 32971, 33042, 33092, 33642, 33672, 33917, 33922, 34078, 34080, 34136, 34437, 34537, 34539, 34654, 34850, 34882, 35029, 35030, 35031, 35234, 35237, 35251, 35367, 35373, 35418, 35620, 35990, 36033, 36215, 36299, 36493, 36495, 36496, 36542, 36652, 36711, 36804, 36868, 36869, 37052, 37205, 37214, 37221, 37260, 37261, 37263, 37405, 37612, 37613, 37656, 37657, 37801, 37847, 37849, 38056, 38063, 38064, 38071, 38235, 38401, 38412, 38679, 38866, 39017, 39135, 39255, 39258, 39271, 39294, 39295, 39297, 39311, 39313, 39314, 39673, 39675, 39679, 39680, 39681, 39744, 39745, 39747, 39748, 40073, 40076, 40077, 40078, 40080, 40082, 40083, 40235, 40319, 40337, 40338, 40616, 40703, 40878, 40952, 40978, 41173, 41174, 41568, 41644, 41703, 41736, 41775, 42007, 42051, 42069, 42377, 42533, 42780, 42991, 42994, 43032, 43238, 43242, 43243, 43244, 43247, 43338, 43348, 43352, 43369, 43370, 43417, 43598, 43599, 43616, 43760, 43762, 43763, 43996, 44012, 44200, 44245, 44447, 44459, 44513, 44535, 44812, 44857, 44859, 45317, 45318, 45704, 45710, 45866, 46093, 46469, 46470, 46473, 46685, 47102, 47152, 47173, 47272, 47601, 47703, 47864, 47880, 47979, 48169, 48439, 48644, 48709, 49487, 49585, 49586, 49592, 49716, 50170]}

    # building_indices = {'Alspaugh': [644], 'Baldwin': [2093, 2094, 20279, 21958, 21987, 21988, 33105, 33124, 33125], 'Bassett': [2902, 2903], 'Blackwell': [4524, 4525, 4529, 4530, 4532, 4534, 4537, 4549, 4550, 4551, 4552, 4553, 4554, 4555, 4556, 4557, 4558, 4559, 4560, 4561, 4562, 4563, 4564, 4565, 4566, 4567, 4568, 4569, 4570, 4571, 4572, 4573, 4574, 4575, 4577, 4578], 'Brodie': [5869], 'Brown': [672, 5635, 6019, 6023, 6045, 6046, 6047, 6049, 6059, 6060, 6062, 6065, 6068, 6069, 6073, 6076, 6077, 6079, 6081, 6082, 6083, 6084, 6123, 6125, 6127, 6134, 6136, 6137, 6138, 6140, 6142, 6145, 6146, 6148, 6150, 6153, 6156, 6157, 6158, 6159, 6160, 6161, 6163, 6164, 6165, 6166, 6167, 6168, 6169, 6170, 6171, 6172, 6173, 6174, 6175, 6176, 6184, 6188, 6192, 6195, 6196, 6198, 6201, 6202, 6206, 6215, 6223, 6224, 6225, 6226, 6240, 6241, 9600, 9605], 'Crowell': [11387], 'Giles': [17234, 17236, 17242, 17243, 43415, 43419, 47180], 'Lilly': [10994, 27597], 'Biddle': [4287, 4291, 4292, 4293, 4296, 4299, 4300, 4314, 4315, 4316, 4317, 4318, 4319, 4320, 4321, 4323, 4324, 38118, 40075], 'Pegram': [35032, 35033, 35034, 35035, 35036], 'Southgate': [42029, 42030, 42067, 42068], 'White': [27817, 48046, 48048, 48050, 48051, 48053, 48054, 48056, 48058, 48059, 48060, 48061, 48062, 48063, 48064, 48065, 48067, 48077, 48086, 48090, 48091, 48092, 48094, 48100, 48101, 48110, 48112, 48114, 48118, 48119, 48120, 48122, 48125, 48126, 48129, 48131, 48133, 48134, 48141, 48143, 48144, 48146], 'Wilson': [7645, 15252, 27146, 33430, 35342, 48955, 48958, 48960, 48961, 48964, 48967, 48968, 48969, 48970, 48971, 48980, 48986, 48987, 48990, 48996, 48998, 49000, 49004, 49007, 49008, 49009, 49019, 49021, 49024, 49028, 49030, 49031, 49034, 49035, 49036, 49038, 49040, 49042, 49043, 49045, 49047, 49049, 49052, 49053, 49056, 49059, 49062, 49064, 49066], 'Allen': [486, 487, 499, 503, 505, 507, 508, 509, 515, 518, 519, 520, 521, 522, 523, 524, 525, 529, 530, 533, 535, 538, 540, 544, 547, 548, 549, 550, 552, 553, 554, 563, 566, 14979, 15511, 17472, 22453, 34964, 35032, 35033, 35034, 35035, 35292, 35293, 37048, 49468], 'Flowers': [15700, 15708, 15710, 15711], 'Gray': [18368, 18369, 18370, 18372, 18375, 18381, 18383, 18386, 18388, 18390, 18391, 18392, 23022], 'Hart': [20569, 20574, 20575, 20577, 20579, 20580, 20582, 20584, 20588, 20593], 'Perkins': [35223, 35226, 35228, 35241, 35243, 35246], 'Rubenstein': [], 'Sanford': [37109, 39311, 39349, 39350, 39355, 39357, 39359, 39360, 39363, 39367], 'Wilkinson': [48566, 48572, 48574, 48575, 48577], 'Craven': [11142, 11146, 11147, 11153, 11154, 11167, 11184, 11192, 11193, 14234], 'Edens': [14394], 'Few': [15285, 15288, 15290, 15293], 'Kilgo': [25715]}

    
    # def get_df_key_index(key,dic):
    #     if key=="All":
    #         return df.iloc[sum(president_indices.values(), [])]
    #     ind = dic[key]
    #     return df.iloc[ind,:]

    # def dataset_selector():
    #     dataset_container = st.sidebar.beta_expander("""Explore Collections Related to Duke's History""", True)
    #     choice = ["Duke University Presidents",
    #         "Duke University Early Names", "Duke University's Buildings"]
    #     with dataset_container:
    #         check = st.radio("Explore",choice)
    #         if check ==choice[0]:
    #             duke_pres = st.selectbox("Select Duke University President ",np.append(np.array("All"),sorted(list(president_indices.keys()))))
    #             return duke_pres,0
    #         elif check == choice[1]:
    #             duke_uni = st.selectbox("Select Duke University's Early Names ",
    #              np.append(np.array("All"),sorted(list(name_indices.keys()))))
    #             return duke_uni,1
    #         else:
    #             duke_buil = st.selectbox("Select Duke University's Buildings in the collection ",
    #              np.append(np.array("All"),sorted(list(building_indices.keys()))))
    #             return duke_buil,2
         

    # def generate_data(selected_identity,explore_topic):
    #     st.write("Display the Duke History Dataframe here")
    #     if(explore_topic==0):
    #         exp_df = get_df_key_index(selected_identity,president_indices)
    #     elif(explore_topic==1):
    #         exp_df = get_df_key_index(selected_identity,name_indices)
    #     else:
    #         exp_df = get_df_key_index(selected_identity,building_indices)
    #     return exp_df

    # selected_identity,explore_topic = dataset_selector()
    # dis = st.beta_container()

    # with dis:
    #     second_container_displayed_df =generate_data(selected_identity,explore_topic)
    #     st.dataframe(second_container_displayed_df)


