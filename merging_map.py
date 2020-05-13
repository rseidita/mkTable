### This file specifies how the merging of salples and/or categories should be performed.
### It may contain one or both the lists "categories_to_merge" and "processes to merge".
### Each one is a list of dicts as in the examples below. "new_name" is the name that
### will be given to the merged procs/cats. "old_names" is a list of procs/cats to be
### merged toghether. Note that these have to exactly correspond to the ones found in the
### input workspace.

# categories_to_merge = [{'new_name' : new_name,
#                         'old_names' : [old_names]}]

# processes_to_merge = [{'new_name' : new_name,
#                        'old_names' : [old_names]}]

olds0j = []
olds1j = []

for charge in ['em_mp', 'em_pm', 'me_mp', 'me_pm']:
    for pt in ['pt2ge20', 'pt2lt20']:
        olds0j.append('ggHtag_of0j_2017_{0}_0j_{1}'.format(charge, pt))
        olds1j.append('ggHtag_of1j_2017_{0}_1j_{1}'.format(charge, pt))

categories_to_merge = [
	{'new_name' : 'ggH_of0j_2017', 'old_names' : olds0j},
        {'new_name' : 'ggH_of1j_2017', 'old_names' : olds1j},
        {'new_name' : 'ggH_of2j_2017', 'old_names' : ['ggHtag_of2j_2017_of2j_2017']},
]

processes_to_merge = [
	{'new_name' : 'DYtot', 'old_names' : ['DY', 'Dyemb']},
        {'new_name' : 'Nonprompt', 'old_names' : ['Fake_em', 'Fake_me']},
        {'new_name' : 'VgS', 'old_names' : ['VgS_H', 'VgS_L']},
]