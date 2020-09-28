region_dict = {
  'USE1' : 'us-east4',
  'USE2' : 'us-central1',
  'USW1' : 'us-west1',
  'USW2' : 'us-west1',
  'UGE1' : 'us-east1',
  'UGW1' : 'us-west1',
  'CPT' : 'us-central1',
  'APE1' : 'asia-east2',
  'APN1' : 'asia-northeast1',
  'APN2' : 'asia-northeast3',
  'APN3' : 'asia-northeast2',
  'APS1' : 'asia-southeast1',
  'APS2' : 'australia-southeast1',
  'APS3' : 'asia-south1',
  'CAN1' : 'us-central1',
  'EUC1' : 'europe-west3',
  'EUW1' : 'europe-west2',
  'EUW2' : 'europe-west2',
  'EUW3' : 'europe-west1',
  'EUN1' : 'europe-north1',
  'EUS1' : 'europe-west3',
  'MES1' : 'us-central1',
  'SAE1' : 'southamerica-east1',
}

compute_ratecard = {
	'box':{
		'n1-predefined-vcpus':{
	      "us": 0.031611,
	      "us-central1": 0.031611,
	      "us-east1": 0.031611,
	      "us-east4": 0.035605,
	      "us-west4": 0.035605,
	      "us-west1": 0.031611,
	      "us-west2": 0.03797,
	      "us-west3": 0.03797,
	      "europe": 0.034773,
	      "europe-west1": 0.034773,
	      "europe-west2": 0.04073,
	      "europe-west3": 0.04073,
	      "europe-west4": 0.0347721,
	      "europe-west6": 0.044231,
	      "europe-north1": 0.034806,
	      "northamerica-northeast1": 0.0347721,
	      "asia": 0.036602,
	      "asia-east": 0.036602,
	      "asia-east1": 0.036602,
	      "asia-east2": 0.044231,
	      "asia-northeast": 0.040618,
	      "asia-northeast1": 0.040618,
	      "asia-northeast2": 0.040618,
	      "asia-northeast3": 0.040618,
	      "asia-southeast": 0.038999,
	      "asia-southeast1": 0.038999,
	      "australia-southeast1": 0.044856,
	      "australia": 0.044856,
	      "southamerica-east1": 0.05018,
	      "asia-south1": 0.03797,
	      "asia-southeast2": 0.04250891
    	},
    	'n1-predefined-memory':{
    	  "us": 0.004237,
	      "us-central1": 0.004237,
	      "us-east1": 0.004237,
	      "us-east4": 0.004771,
	      "us-west4": 0.004771,
	      "us-west1": 0.004237,
	      "us-west2": 0.005089,
	      "us-west3": 0.005089,
	      "europe": 0.004661,
	      "europe-west1": 0.004661,
	      "europe-west2": 0.005458,
	      "europe-west3": 0.005458,
	      "europe-west4": 0.0046607,
	      "europe-west6": 0.005928,
	      "europe-north1": 0.004664,
	      "northamerica-northeast1": 0.00444885,
	      "asia": 0.004906,
	      "asia-east": 0.004906,
	      "asia-east1": 0.004906,
	      "asia-east2": 0.005928,
	      "asia-northeast": 0.005419,
	      "asia-northeast1": 0.005419,
	      "asia-northeast2": 0.005419,
	      "asia-northeast3": 0.005419,
	      "asia-southeast": 0.005226,
	      "asia-southeast1": 0.005226,
	      "australia-southeast1": 0.006011,
	      "australia": 0.006011,
	      "southamerica-east1": 0.006725,
	      "asia-south1": 0.005088,
	      "asia-southeast2": 0.00569634
    	},
    	'n1-custom-vcpus':{
	      "us": 0.033174,
	      "us-central1": 0.033174,
	      "us-east1": 0.033174,
	      "us-east4": 0.037364,
	      "us-west4": 0.037364,
	      "us-west1": 0.033174,
	      "us-west2": 0.03797,
	      "us-west3": 0.03797,
	      "europe": 0.036489,
	      "europe-west1": 0.036489,
	      "europe-west2": 0.040692,
	      "europe-west3": 0.040692,
	      "europe-west4": 0.034802,
	      "europe-west6": 0.044231,
	      "europe-north1": 0.034802,
	      "northamerica-northeast1": 0.034802,
	      "asia": 0.03841,
	      "asia-east": 0.03841,
	      "asia-east1": 0.03841,
	      "asia-east2": 0.044231,
	      "asia-northeast": 0.040618,
	      "asia-northeast1": 0.040618,
	      "asia-northeast2": 0.040618,
	      "asia-northeast3": 0.040618,
	      "asia-southeast": 0.038996,
	      "asia-southeast1": 0.038996,
	      "australia-southeast1": 0.04488,
	      "australia": 0.04488,
	      "southamerica-east1": 0.05019,
	      "asia-south1": 0.037966,
	      "asia-southeast2": 0.04250564
	    },
	    'n1-custom-memory':{
	      "us": 0.004446,
	      "us-central1": 0.004446,
	      "us-east1": 0.004446,
	      "us-east4": 0.005008,
	      "us-west4": 0.005008,
	      "us-west1": 0.004446,
	      "us-west2": 0.005089,
	      "us-west3": 0.005089,
	      "europe": 0.004892,
	      "europe-west1": 0.004892,
	      "europe-west2": 0.005453,
	      "europe-west3": 0.005453,
	      "europe-west4": 0.004664,
	      "europe-west6": 0.005928,
	      "europe-north1": 0.004664,
	      "northamerica-northeast1": 0.004664,
	      "asia": 0.00515,
	      "asia-east": 0.00515,
	      "asia-east1": 0.00515,
	      "asia-east2": 0.005928,
	      "asia-northeast": 0.005418,
	      "asia-northeast1": 0.005418,
	      "asia-northeast2": 0.005418,
	      "asia-northeast3": 0.005418,
	      "asia-southeast": 0.005226,
	      "asia-southeast1": 0.005226,
	      "australia-southeast1": 0.00601,
	      "australia": 0.00601,
	      "southamerica-east1": 0.006729,
	      "asia-south1": 0.005088,
	      "asia-southeast2": 0.00569634
	    },
	    'e2-predefined-vcpus':{
	      "us": 0.02181159,
	      "asia-east2": 0.03051939,
	      "asia-east1": 0.02525538,
	      "asia": 0.02525538,
	      "europe-north1": 0.02401614,
	      "us-central1": 0.02181159,
	      "asia-east": 0.02525538,
	      "asia-northeast": 0.02802642,
	      "europe": 0.02399337,
	      "australia-southeast1": 0.03095064,
	      "australia": 0.03095064,
	      "asia-south1": 0.0261993,
	      "us-west1": 0.02181159,
	      "us-west2": 0.0261993,
	      "us-west3": 0.0261993,
	      "asia-northeast2": 0.02802642,
	      "asia-northeast3": 0.02802642,
	      "asia-northeast1": 0.02802642,
	      "asia-southeast": 0.02690931,
	      "asia-southeast1": 0.02690931,
	      "europe-west2": 0.0281037,
	      "europe-west3": 0.0281037,
	      "us-east4": 0.02456745,
	      "us-west4": 0.02456745,
	      "europe-west1": 0.02399337,
	      "europe-west6": 0.03051939,
	      "europe-west4": 0.02401338,
	      "us-east1": 0.02181159,
	      "northamerica-northeast1": 0.02401338,
	      "southamerica-east1": 0.0346242,
	      "asia-southeast2": 0.0293311479
	    },
	    'e2-predefined-memory':{
	      "us": 0.00292353,
	      "asia-east2": 0.00409032,
	      "asia-east1": 0.00338514,
	      "asia": 0.00338514,
	      "europe-north1": 0.00321816,
	      "us-central1": 0.00292353,
	      "asia-east": 0.00338514,
	      "asia-northeast": 0.00373911,
	      "europe": 0.00321609,
	      "australia-southeast1": 0.00414759,
	      "australia": 0.00414759,
	      "asia-south1": 0.00351072,
	      "us-west1": 0.00292353,
	      "us-west2": 0.00351141,
	      "us-west3": 0.00351141,
	      "asia-northeast2": 0.00373911,
	      "asia-northeast3": 0.00373911,
	      "asia-northeast1": 0.00373911,
	      "asia-southeast": 0.00360594,
	      "asia-southeast1": 0.00360594,
	      "europe-west2": 0.00376602,
	      "europe-west3": 0.00376602,
	      "us-east4": 0.00329199,
	      "us-west4": 0.00329199,
	      "europe-west1": 0.00321609,
	      "europe-west6": 0.00409032,
	      "europe-west4": 0.00321816,
	      "us-east1": 0.00292353,
	      "northamerica-northeast1": 0.00321816,
	      "southamerica-east1": 0.00464025,
	      "asia-southeast2": 0.0039304746
	    },
	    'e2-micro':{
	      "us": 0.00838,
	      "asia-east2": 0.01172,
	      "asia-east1": 0.0097,
	      "asia": 0.0097,
	      "europe-north1": 0.00922,
	      "us-central1": 0.00838,
	      "asia-northeast": 0.01075,
	      "europe": 0.00921,
	      "australia-southeast1": 0.01189,
	      "australia": 0.01189,
	      "asia-south1": 0.01006,
	      "us-west1": 0.00838,
	      "us-west2": 0.01006,
	      "us-west3": 0.01006,
	      "asia-east": 0.0097,
	      "asia-northeast2": 0,
	      "asia-northeast3": 0,
	      "asia-northeast1": 0.01075,
	      "asia-southeast": 0.01033,
	      "asia-southeast1": 0.01033,
	      "europe-west2": 0.01079,
	      "europe-west3": 0.01079,
	      "us-east4": 0.00943,
	      "us-west4": 0.00943,
	      "europe-west1": 0.00921,
	      "europe-west6": 0,
	      "europe-west4": 0.00922,
	      "us-east1": 0.00838,
	      "northamerica-northeast1": 0.00922,
	      "southamerica-east1": 0.0133,
	      "cores": "0.25",
	      "memory": "1",
	      "asia-southeast2": 0.0112597
	    },
	    'e2-small':{
	      "us": 0.01675,
	      "asia-east2": 0.02344,
	      "asia-east1": 0.0194,
	      "asia": 0.0194,
	      "europe-north1": 0.01844,
	      "us-central1": 0.01675,
	      "asia-northeast": 0.02149,
	      "europe": 0.01843,
	      "australia-southeast1": 0.02377,
	      "australia": 0.02377,
	      "asia-south1": 0.02012,
	      "us-west1": 0.01675,
	      "us-west2": 0.02012,
	      "us-west3": 0.02012,
	      "asia-east": 0.0194,
	      "asia-northeast2": 0,
	      "asia-northeast3": 0,
	      "asia-northeast1": 0.02149,
	      "asia-southeast": 0.02067,
	      "asia-southeast1": 0.02067,
	      "europe-west2": 0.02158,
	      "europe-west3": 0.02158,
	      "us-east4": 0.01887,
	      "us-west4": 0.01887,
	      "europe-west1": 0.01843,
	      "europe-west6": 0,
	      "europe-west4": 0.01844,
	      "us-east1": 0.01675,
	      "northamerica-northeast1": 0.01844,
	      "southamerica-east1": 0.02659,
	      "cores": "0.5",
	      "memory": "2",
	      "asia-southeast2": 0.0225303
	    },
	    'e2-medium':{
	      "us": 0.03351,
	      "asia-east2": 0.04688,
	      "asia-east1": 0.0388,
	      "asia": 0.0388,
	      "europe-north1": 0.03689,
	      "us-central1": 0.03351,
	      "asia-northeast": 0.04298,
	      "europe": 0.03686,
	      "australia-southeast1": 0.04754,
	      "australia": 0.04754,
	      "asia-south1": 0.04024,
	      "us-west1": 0.03351,
	      "us-west2": 0.04024,
	      "us-west3": 0.04024,
	      "asia-east": 0.0388,
	      "asia-northeast2": 0,
	      "asia-northeast3": 0,
	      "asia-northeast1": 0.04298,
	      "asia-southeast": 0.04133,
	      "asia-southeast1": 0.04133,
	      "europe-west2": 0.04317,
	      "europe-west3": 0.04317,
	      "us-east4": 0.03774,
	      "us-west4": 0.03774,
	      "europe-west1": 0.03686,
	      "europe-west6": 0,
	      "europe-west4": 0.03689,
	      "us-east1": 0.03351,
	      "northamerica-northeast1": 0.03689,
	      "southamerica-east1": 0.05319,
	      "cores": "1",
	      "memory": "4",
	      "asia-southeast2": 0.0450497
	    },
	    'f1-micro':{
	      "us": 0.0076,
	      "us-central1": 0.0076,
	      "us-east1": 0.0076,
	      "us-east4": 0.0086,
	      "us-west4": 0.0086,
	      "us-west1": 0.0076,
	      "us-west2": 0.0091,
	      "us-west3": 0.0091,
	      "europe": 0.0086,
	      "europe-west1": 0.0086,
	      "europe-west2": 0.0096,
	      "europe-west3": 0.0096,
	      "europe-west4": 0.0084,
	      "europe-west6": 0.0106,
	      "europe-north1": 0.0084,
	      "northamerica-northeast1": 0.0084,
	      "asia": 0.009,
	      "asia-east": 0.009,
	      "asia-east1": 0.009,
	      "asia-east2": 0.0106,
	      "asia-northeast": 0.0092,
	      "asia-northeast1": 0.0092,
	      "asia-northeast2": 0.0092,
	      "asia-northeast3": 0.0092,
	      "asia-southeast": 0.0092,
	      "asia-southeast1": 0.0092,
	      "australia-southeast1": 0.0106,
	      "australia": 0.0106,
	      "southamerica-east1": 0.0118,
	      "asia-south1": 0.0091,
	      "cores": "shared",
	      "memory": "0.6",
	      "gceu": "Shared CPU, not guaranteed",
	      "maxNumberOfPd": 16,
	      "maxPdSize": 64,
	      "ssd": [
	        0
	      ],
	      "asia-southeast2": 0.010028
	    },
	    'g1-small':{
	      "us": 0.027,
	      "us-central1": 0.027,
	      "us-east1": 0.027,
	      "us-east4": 0.0289,
	      "us-west4": 0.0289,
	      "us-west1": 0.027,
	      "us-west2": 0.0308,
	      "us-west3": 0.0308,
	      "europe": 0.0285,
	      "europe-west1": 0.0285,
	      "europe-west2": 0.0324,
	      "europe-west3": 0.0324,
	      "europe-west4": 0.0283,
	      "europe-west6": 0.0359,
	      "europe-north1": 0.0283,
	      "northamerica-northeast1": 0.0283,
	      "asia": 0.03,
	      "asia-east": 0.03,
	      "asia-east1": 0.03,
	      "asia-east2": 0.0359,
	      "asia-northeast": 0.0322,
	      "asia-northeast1": 0.0322,
	      "asia-northeast2": 0.0322,
	      "asia-northeast3": 0.0322,
	      "asia-southeast": 0.0311,
	      "asia-southeast1": 0.0311,
	      "australia-southeast1": 0.0357,
	      "australia": 0.0357,
	      "southamerica-east1": 0.04,
	      "asia-south1": 0.0308,
	      "cores": "shared",
	      "memory": "1.7",
	      "gceu": 1.38,
	      "maxNumberOfPd": 16,
	      "maxPdSize": 64,
	      "ssd": [
	        0
	      ],
	      "asia-southeast2": 0.033899
	    },
	},
	'heavy':{
		'n1-predefined-vcpus':{
	      "us": 0.019915,
	      "us-central1": 0.019915,
	      "us-east1": 0.019915,
	      "us-east4": 0.021309,
	      "us-west4": 0.021309,
	      "us-west1": 0.019915,
	      "us-west2": 0.023921,
	      "us-west3": 0.023921,
	      "europe": 0.021907,
	      "europe-west1": 0.021907,
	      "europe-west2": 0.025636,
	      "europe-west3": 0.025636,
	      "europe-west4": 0.021925,
	      "europe-west6": 0.027866,
	      "europe-north1": 0.021925,
	      "northamerica-northeast1": 0.021925,
	      "asia-east": 0.023059,
	      "asia-east1": 0.023059,
	      "asia-east2": 0.027866,
	      "asia-northeast": 0.025589,
	      "asia-northeast1": 0.025589,
	      "asia-northeast2": 0.025589,
	      "asia-northeast3": 0.025589,
	      "asia-southeast": 0.024567,
	      "asia-southeast1": 0.024567,
	      "australia-southeast1": 0.028274,
	      "australia": 0.028274,
	      "southamerica-east1": 0.03162,
	      "asia-south1": 0.023919,
	      "asia-southeast2": 0.02677803
	    },
	    'n1-predefined-memory':{
	      "us": 0.002669,
	      "us-central1": 0.002669,
	      "us-east1": 0.002669,
	      "us-east4": 0.002856,
	      "us-west4": 0.002856,
	      "us-west1": 0.002669,
	      "us-west2": 0.003206,
	      "us-west3": 0.003206,
	      "europe": 0.002936,
	      "europe-west1": 0.002936,
	      "europe-west2": 0.003435,
	      "europe-west3": 0.003435,
	      "europe-west4": 0.002938,
	      "europe-west6": 0.003735,
	      "europe-north1": 0.002938,
	      "northamerica-northeast1": 0.002938,
	      "asia-east": 0.003091,
	      "asia-east1": 0.003091,
	      "asia-east2": 0.003735,
	      "asia-northeast": 0.003414,
	      "asia-northeast1": 0.003414,
	      "asia-northeast2": 0.003414,
	      "asia-northeast3": 0.003414,
	      "asia-southeast": 0.003292,
	      "asia-southeast1": 0.003292,
	      "australia-southeast1": 0.003786,
	      "australia": 0.003786,
	      "southamerica-east1": 0.004239,
	      "asia-south1": 0.003205,
	      "asia-southeast2": 0.00358828
	    },
	    'n1-custom-vcpus':{#Same as predifined
	      "us": 0.019915,
	      "us-central1": 0.019915,
	      "us-east1": 0.019915,
	      "us-east4": 0.021309,
	      "us-west4": 0.021309,
	      "us-west1": 0.019915,
	      "us-west2": 0.023921,
	      "us-west3": 0.023921,
	      "europe": 0.021907,
	      "europe-west1": 0.021907,
	      "europe-west2": 0.025636,
	      "europe-west3": 0.025636,
	      "europe-west4": 0.021925,
	      "europe-west6": 0.027866,
	      "europe-north1": 0.021925,
	      "northamerica-northeast1": 0.021925,
	      "asia-east": 0.023059,
	      "asia-east1": 0.023059,
	      "asia-east2": 0.027866,
	      "asia-northeast": 0.025589,
	      "asia-northeast1": 0.025589,
	      "asia-northeast2": 0.025589,
	      "asia-northeast3": 0.025589,
	      "asia-southeast": 0.024567,
	      "asia-southeast1": 0.024567,
	      "australia-southeast1": 0.028274,
	      "australia": 0.028274,
	      "southamerica-east1": 0.03162,
	      "asia-south1": 0.023919,
	      "asia-southeast2": 0.02677803
	    },
	    'n1-custom-memory':{#Same as predefined
	      "us": 0.002669,
	      "us-central1": 0.002669,
	      "us-east1": 0.002669,
	      "us-east4": 0.002856,
	      "us-west4": 0.002856,
	      "us-west1": 0.002669,
	      "us-west2": 0.003206,
	      "us-west3": 0.003206,
	      "europe": 0.002936,
	      "europe-west1": 0.002936,
	      "europe-west2": 0.003435,
	      "europe-west3": 0.003435,
	      "europe-west4": 0.002938,
	      "europe-west6": 0.003735,
	      "europe-north1": 0.002938,
	      "northamerica-northeast1": 0.002938,
	      "asia-east": 0.003091,
	      "asia-east1": 0.003091,
	      "asia-east2": 0.003735,
	      "asia-northeast": 0.003414,
	      "asia-northeast1": 0.003414,
	      "asia-northeast2": 0.003414,
	      "asia-northeast3": 0.003414,
	      "asia-southeast": 0.003292,
	      "asia-southeast1": 0.003292,
	      "australia-southeast1": 0.003786,
	      "australia": 0.003786,
	      "southamerica-east1": 0.004239,
	      "asia-south1": 0.003205,
	      "asia-southeast2": 0.00358828
	    },
	    'e2-predefined-vcpus':{
	      "us": 0.013741302,
	      "asia-east2": 0.019227216,
	      "asia-east1": 0.015910889,
	      "asia": 0.015910889,
	      "europe-north1": 0.015130168,
	      "us-central1": 0.013741302,
	      "asia-east": 0.015910889,
	      "asia-northeast": 0.017656645,
	      "europe": 0.015115823,
	      "australia-southeast1": 0.019498903,
	      "australia": 0.019498903,
	      "asia-south1": 0.016505559,
	      "us-west1": 0.013741302,
	      "us-west2": 0.016505559,
	      "us-west3": 0.016505559,
	      "asia-northeast2": 0.017656645,
	      "asia-northeast3": 0.017656645,
	      "asia-northeast1": 0.017656645,
	      "asia-southeast": 0.016952865,
	      "asia-southeast1": 0.016952865,
	      "europe-west2": 0.017705331,
	      "europe-west3": 0.017705331,
	      "us-east4": 0.015477494,
	      "us-west4": 0.015477494,
	      "europe-west1": 0.015115823,
	      "europe-west6": 0.019227215,
	      "europe-west4": 0.015128429,
	      "us-east1": 0.013741302,
	      "northamerica-northeast1": 0.015128429,
	      "southamerica-east1": 0.021813246,
	      "asia-southeast2": 0.01847862285
	    },
	    'e2-predefined-memory':{
	      "us": 0.001841824,
	      "asia-east2": 0.002576902,
	      "asia-east1": 0.002132638,
	      "asia": 0.002132638,
	      "europe-north1": 0.002027441,
	      "us-central1": 0.001841824,
	      "asia-east": 0.002132638,
	      "asia-northeast": 0.002355639,
	      "europe": 0.002026137,
	      "australia-southeast1": 0.002612982,
	      "australia": 0.002612982,
	      "asia-south1": 0.002211754,
	      "us-west1": 0.001841824,
	      "us-west2": 0.002212188,
	      "us-west3": 0.002212188,
	      "asia-northeast2": 0.002355639,
	      "asia-northeast3": 0.002355639,
	      "asia-northeast1": 0.002355639,
	      "asia-southeast": 0.002271742,
	      "asia-southeast1": 0.002271742,
	      "europe-west2": 0.002372593,
	      "europe-west3": 0.002372593,
	      "us-east4": 0.002073954,
	      "us-west4": 0.002073954,
	      "europe-west1": 0.002026137,
	      "europe-west6": 0.002576901,
	      "europe-west4": 0.002027441,
	      "us-east1": 0.001841824,
	      "northamerica-northeast1": 0.002027441,
	      "southamerica-east1": 0.002923358,
	      "asia-southeast2": 0.00247619878
	    },
	    'e2-micro':{#Same as box
	      "us": 0.00838,
	      "asia-east2": 0.01172,
	      "asia-east1": 0.0097,
	      "asia": 0.0097,
	      "europe-north1": 0.00922,
	      "us-central1": 0.00838,
	      "asia-northeast": 0.01075,
	      "europe": 0.00921,
	      "australia-southeast1": 0.01189,
	      "australia": 0.01189,
	      "asia-south1": 0.01006,
	      "us-west1": 0.00838,
	      "us-west2": 0.01006,
	      "us-west3": 0.01006,
	      "asia-east": 0.0097,
	      "asia-northeast2": 0,
	      "asia-northeast3": 0,
	      "asia-northeast1": 0.01075,
	      "asia-southeast": 0.01033,
	      "asia-southeast1": 0.01033,
	      "europe-west2": 0.01079,
	      "europe-west3": 0.01079,
	      "us-east4": 0.00943,
	      "us-west4": 0.00943,
	      "europe-west1": 0.00921,
	      "europe-west6": 0,
	      "europe-west4": 0.00922,
	      "us-east1": 0.00838,
	      "northamerica-northeast1": 0.00922,
	      "southamerica-east1": 0.0133,
	      "cores": "0.25",
	      "memory": "1",
	      "asia-southeast2": 0.0112597
	    },
	    'e2-small':{#Same as box
	      "us": 0.01675,
	      "asia-east2": 0.02344,
	      "asia-east1": 0.0194,
	      "asia": 0.0194,
	      "europe-north1": 0.01844,
	      "us-central1": 0.01675,
	      "asia-northeast": 0.02149,
	      "europe": 0.01843,
	      "australia-southeast1": 0.02377,
	      "australia": 0.02377,
	      "asia-south1": 0.02012,
	      "us-west1": 0.01675,
	      "us-west2": 0.02012,
	      "us-west3": 0.02012,
	      "asia-east": 0.0194,
	      "asia-northeast2": 0,
	      "asia-northeast3": 0,
	      "asia-northeast1": 0.02149,
	      "asia-southeast": 0.02067,
	      "asia-southeast1": 0.02067,
	      "europe-west2": 0.02158,
	      "europe-west3": 0.02158,
	      "us-east4": 0.01887,
	      "us-west4": 0.01887,
	      "europe-west1": 0.01843,
	      "europe-west6": 0,
	      "europe-west4": 0.01844,
	      "us-east1": 0.01675,
	      "northamerica-northeast1": 0.01844,
	      "southamerica-east1": 0.02659,
	      "cores": "0.5",
	      "memory": "2",
	      "asia-southeast2": 0.0225303
	    },
	    'e2-medium':{#Same as box
	      "us": 0.03351,
	      "asia-east2": 0.04688,
	      "asia-east1": 0.0388,
	      "asia": 0.0388,
	      "europe-north1": 0.03689,
	      "us-central1": 0.03351,
	      "asia-northeast": 0.04298,
	      "europe": 0.03686,
	      "australia-southeast1": 0.04754,
	      "australia": 0.04754,
	      "asia-south1": 0.04024,
	      "us-west1": 0.03351,
	      "us-west2": 0.04024,
	      "us-west3": 0.04024,
	      "asia-east": 0.0388,
	      "asia-northeast2": 0,
	      "asia-northeast3": 0,
	      "asia-northeast1": 0.04298,
	      "asia-southeast": 0.04133,
	      "asia-southeast1": 0.04133,
	      "europe-west2": 0.04317,
	      "europe-west3": 0.04317,
	      "us-east4": 0.03774,
	      "us-west4": 0.03774,
	      "europe-west1": 0.03686,
	      "europe-west6": 0,
	      "europe-west4": 0.03689,
	      "us-east1": 0.03351,
	      "northamerica-northeast1": 0.03689,
	      "southamerica-east1": 0.05319,
	      "cores": "1",
	      "memory": "4",
	      "asia-southeast2": 0.0450497
	    },
	    'f1-micro':{#Same as box
	      "us": 0.0076,
	      "us-central1": 0.0076,
	      "us-east1": 0.0076,
	      "us-east4": 0.0086,
	      "us-west4": 0.0086,
	      "us-west1": 0.0076,
	      "us-west2": 0.0091,
	      "us-west3": 0.0091,
	      "europe": 0.0086,
	      "europe-west1": 0.0086,
	      "europe-west2": 0.0096,
	      "europe-west3": 0.0096,
	      "europe-west4": 0.0084,
	      "europe-west6": 0.0106,
	      "europe-north1": 0.0084,
	      "northamerica-northeast1": 0.0084,
	      "asia": 0.009,
	      "asia-east": 0.009,
	      "asia-east1": 0.009,
	      "asia-east2": 0.0106,
	      "asia-northeast": 0.0092,
	      "asia-northeast1": 0.0092,
	      "asia-northeast2": 0.0092,
	      "asia-northeast3": 0.0092,
	      "asia-southeast": 0.0092,
	      "asia-southeast1": 0.0092,
	      "australia-southeast1": 0.0106,
	      "australia": 0.0106,
	      "southamerica-east1": 0.0118,
	      "asia-south1": 0.0091,
	      "cores": "shared",
	      "memory": "0.6",
	      "gceu": "Shared CPU, not guaranteed",
	      "maxNumberOfPd": 16,
	      "maxPdSize": 64,
	      "ssd": [
	        0
	      ],
	      "asia-southeast2": 0.010028
	    },
	    'g1-small':{#Same as box
	      "us": 0.027,
	      "us-central1": 0.027,
	      "us-east1": 0.027,
	      "us-east4": 0.0289,
	      "us-west4": 0.0289,
	      "us-west1": 0.027,
	      "us-west2": 0.0308,
	      "us-west3": 0.0308,
	      "europe": 0.0285,
	      "europe-west1": 0.0285,
	      "europe-west2": 0.0324,
	      "europe-west3": 0.0324,
	      "europe-west4": 0.0283,
	      "europe-west6": 0.0359,
	      "europe-north1": 0.0283,
	      "northamerica-northeast1": 0.0283,
	      "asia": 0.03,
	      "asia-east": 0.03,
	      "asia-east1": 0.03,
	      "asia-east2": 0.0359,
	      "asia-northeast": 0.0322,
	      "asia-northeast1": 0.0322,
	      "asia-northeast2": 0.0322,
	      "asia-northeast3": 0.0322,
	      "asia-southeast": 0.0311,
	      "asia-southeast1": 0.0311,
	      "australia-southeast1": 0.0357,
	      "australia": 0.0357,
	      "southamerica-east1": 0.04,
	      "asia-south1": 0.0308,
	      "cores": "shared",
	      "memory": "1.7",
	      "gceu": 1.38,
	      "maxNumberOfPd": 16,
	      "maxPdSize": 64,
	      "ssd": [
	        0
	      ],
	      "asia-southeast2": 0.033899
	    },
	},
	'spot':{
		'n1-predefined-vcpus':{
	      "us": 0.006655,
	      "us-central1": 0.006655,
	      "us-east1": 0.006655,
	      "us-east4": 0.00712085,
	      "us-west4": 0.00712085,
	      "us-west1": 0.006655,
	      "us-west2": 0.007617,
	      "us-west3": 0.007617,
	      "europe": 0.007321,
	      "europe-west1": 0.007321,
	      "europe-west2": 0.00815,
	      "europe-west3": 0.00815,
	      "europe-west4": 0.007321,
	      "europe-west6": 0.009309,
	      "europe-north1": 0.007321,
	      "northamerica-northeast1": 0.007321,
	      "asia": 0.00732,
	      "asia-east": 0.00732,
	      "asia-east1": 0.00732,
	      "asia-east2": 0.009309,
	      "asia-northeast": 0.00883,
	      "asia-northeast1": 0.00883,
	      "asia-northeast2": 0.00883,
	      "asia-northeast3": 0.00883,
	      "asia-southeast": 0.0078,
	      "asia-southeast1": 0.0078,
	      "australia-southeast1": 0.0089,
	      "australia": 0.0089,
	      "southamerica-east1": 0.00998265,
	      "asia-south1": 0.0080004,
	      "asia-southeast2": 0.008502
	    },
	    'n1-predefined-memory':{
	      "us": 0.000892,
	      "us-central1": 0.000892,
	      "us-east1": 0.000892,
	      "us-east4": 0.00095444,
	      "us-west4": 0.00095444,
	      "us-west1": 0.000892,
	      "us-west2": 0.001021,
	      "us-west3": 0.001021,
	      "europe": 0.000981,
	      "europe-west1": 0.000981,
	      "europe-west2": 0.00109,
	      "europe-west3": 0.00109,
	      "europe-west4": 0.000981,
	      "europe-west6": 0.001254,
	      "europe-north1": 0.000981,
	      "northamerica-northeast1": 0.000981,
	      "asia": 0.000981,
	      "asia-east": 0.000981,
	      "asia-east1": 0.000981,
	      "asia-east2": 0.001254,
	      "asia-northeast": 0.001178,
	      "asia-northeast1": 0.001178,
	      "asia-northeast2": 0.001178,
	      "asia-northeast3": 0.001178,
	      "asia-southeast": 0.00105,
	      "asia-southeast1": 0.00105,
	      "australia-southeast1": 0.0012,
	      "australia": 0.0012,
	      "southamerica-east1": 0.001338,
	      "asia-south1": 0.00107454,
	      "asia-southeast2": 0.0011445
	    },
	    'n1-custom-vcpus':{
	      "us": 0.00698,
	      "us-central1": 0.00698,
	      "us-east1": 0.00698,
	      "us-east4": 0.007469,
	      "us-west4": 0.007469,
	      "us-west1": 0.00698,
	      "us-west2": 0.007986,
	      "us-west3": 0.007986,
	      "europe": 0.00768,
	      "europe-west1": 0.00768,
	      "europe-west2": 0.00815,
	      "europe-west3": 0.00815,
	      "europe-west4": 0.007325,
	      "europe-west6": 0.009309,
	      "europe-north1": 0.007325,
	      "northamerica-northeast1": 0.007325,
	      "asia": 0.00768,
	      "asia-east": 0.00768,
	      "asia-east1": 0.00768,
	      "asia-east2": 0.009309,
	      "asia-northeast": 0.00883,
	      "asia-northeast1": 0.00883,
	      "asia-northeast2": 0.00883,
	      "asia-northeast3": 0.00883,
	      "asia-southeast": 0.007801,
	      "asia-southeast1": 0.007801,
	      "australia-southeast1": 0.00898,
	      "australia": 0.00898,
	      "southamerica-east1": 0.010038,
	      "asia-south1": 0.007992,
	      "asia-southeast2": 0.00850309
	    },
	    'n1-custom-memory':{
	      "us": 0.00094,
	      "us-central1": 0.00094,
	      "us-east1": 0.00094,
	      "us-east4": 0.001006,
	      "us-west4": 0.001006,
	      "us-west1": 0.00094,
	      "us-west2": 0.001076,
	      "us-west3": 0.001076,
	      "europe": 0.00103,
	      "europe-west1": 0.00103,
	      "europe-west2": 0.00109,
	      "europe-west3": 0.00109,
	      "europe-west4": 0.000987,
	      "europe-west6": 0.001254,
	      "europe-north1": 0.000981,
	      "northamerica-northeast1": 0.000987,
	      "asia": 0.00103,
	      "asia-east": 0.00103,
	      "asia-east1": 0.00103,
	      "asia-east2": 0.001254,
	      "asia-northeast": 0.001178,
	      "asia-northeast1": 0.001178,
	      "asia-northeast2": 0.001178,
	      "asia-northeast3": 0.001178,
	      "asia-southeast": 0.001045,
	      "asia-southeast1": 0.001045,
	      "australia-southeast1": 0.0012,
	      "australia": 0.0012,
	      "southamerica-east1": 0.001346,
	      "asia-south1": 0.001076,
	      "asia-southeast2": 0.00113905
	    },
	    'e2-predefined-vcpus':{
	      "us": 0.006543477,
	      "asia-east2": 0.009155817,
	      "asia-east1": 0.007576614,
	      "asia": 0.007576614,
	      "europe-north1": 0.007204842,
	      "us-central1": 0.006543477,
	      "asia-east": 0.007576614,
	      "asia-northeast": 0.008407926,
	      "europe": 0.007198011,
	      "australia-southeast1": 0.009285192,
	      "australia": 0.009285192,
	      "asia-south1": 0.00785979,
	      "us-west1": 0.006543477,
	      "us-west2": 0.00785979,
	      "us-west3": 0.00785979,
	      "asia-northeast2": 0.008407926,
	      "asia-northeast3": 0.008407926,
	      "asia-northeast1": 0.008407926,
	      "asia-southeast": 0.008072793,
	      "asia-southeast1": 0.008072793,
	      "europe-west2": 0.00843111,
	      "europe-west3": 0.00843111,
	      "us-east4": 0.007370235,
	      "us-west4": 0.007370235,
	      "europe-west1": 0.007198011,
	      "europe-west6": 0.009155817,
	      "europe-west4": 0.007204014,
	      "us-east1": 0.006543477,
	      "northamerica-northeast1": 0.007204014,
	      "southamerica-east1": 0.01038726,
	      "asia-southeast2": 0.00879934437
	    },
	    'e2-predefined-memory':{
	      "us": 0.000877059,
	      "asia-east2": 0.001227096,
	      "asia-east1": 0.001015542,
	      "asia": 0.001015542,
	      "europe-north1": 0.000965448,
	      "us-central1": 0.000877059,
	      "asia-east": 0.001015542,
	      "asia-northeast": 0.001121733,
	      "europe": 0.000964827,
	      "australia-southeast1": 0.001244277,
	      "australia": 0.001244277,
	      "asia-south1": 0.001053216,
	      "us-west1": 0.000877059,
	      "us-west2": 0.001053423,
	      "us-west3": 0.001053423,
	      "asia-northeast2": 0.001121733,
	      "asia-northeast3": 0.001121733,
	      "asia-northeast1": 0.001121733,
	      "asia-southeast": 0.001081782,
	      "asia-southeast1": 0.001081782,
	      "europe-west2": 0.001129806,
	      "europe-west3": 0.001129806,
	      "us-east4": 0.000987597,
	      "us-west4": 0.000987597,
	      "europe-west1": 0.000964827,
	      "europe-west6": 0.001121733,
	      "europe-west4": 0.000965448,
	      "us-east1": 0.000877059,
	      "northamerica-northeast1": 0.000965448,
	      "southamerica-east1": 0.001392075,
	      "asia-southeast2": 0.00117914238
	    },
	    'e2-micro':{
	      "us": 0.00251,
	      "asia-east2": 0.00352,
	      "asia-east1": 0.00291,
	      "asia": 0.00291,
	      "europe-north1": 0.00277,
	      "us-central1": 0.00251,
	      "asia-northeast": 0.00322,
	      "europe": 0.00276,
	      "australia-southeast1": 0.00357,
	      "australia": 0.00357,
	      "asia-south1": 0.00302,
	      "us-west1": 0.00251,
	      "us-west2": 0.00302,
	      "us-west3": 0.00302,
	      "asia-east": 0.00291,
	      "asia-northeast2": 0,
	      "asia-northeast3": 0,
	      "asia-northeast1": 0.00322,
	      "asia-southeast": 0.0031,
	      "asia-southeast1": 0.0031,
	      "europe-west2": 0.00324,
	      "europe-west3": 0.00324,
	      "us-east4": 0.00283,
	      "us-west4": 0.00283,
	      "europe-west1": 0.00276,
	      "europe-west6": 0,
	      "europe-west4": 0.00277,
	      "us-east1": 0.00251,
	      "northamerica-northeast1": 0.00277,
	      "southamerica-east1": 0.00399,
	      "cores": "0.25",
	      "memory": "1",
	      "asia-southeast2": 0.003379
	    },
	    'e2-small':{
	      "us": 0.00503,
	      "asia-east2": 0.00703,
	      "asia-east1": 0.00582,
	      "asia": 0.00582,
	      "europe-north1": 0.00553,
	      "us-central1": 0.00503,
	      "asia-northeast": 0.00645,
	      "europe": 0.00553,
	      "australia-southeast1": 0.00713,
	      "australia": 0.00713,
	      "asia-south1": 0.00604,
	      "us-west1": 0.00503,
	      "us-west2": 0.00604,
	      "us-west3": 0.00604,
	      "asia-east": 0.00582,
	      "asia-northeast2": 0,
	      "asia-northeast3": 0,
	      "asia-northeast1": 0.00645,
	      "asia-southeast": 0.0062,
	      "asia-southeast1": 0.0062,
	      "europe-west2": 0.00648,
	      "europe-west3": 0.00648,
	      "us-east4": 0.00566,
	      "us-west4": 0.00566,
	      "europe-west1": 0.00553,
	      "europe-west6": 0,
	      "europe-west4": 0.00553,
	      "us-east1": 0.00503,
	      "northamerica-northeast1": 0.00553,
	      "southamerica-east1": 0.00798,
	      "cores": "0.5",
	      "memory": "2",
	      "asia-southeast2": 0.006758
	    },
	    'e2-medium':{
	      "us": 0.01005,
	      "asia-east2": 0.01406,
	      "asia-east1": 0.01164,
	      "asia": 0.01164,
	      "europe-north1": 0.01107,
	      "us-central1": 0.01005,
	      "asia-northeast": 0.01289,
	      "europe": 0.01106,
	      "australia-southeast1": 0.01426,
	      "australia": 0.01426,
	      "asia-south1": 0.01207,
	      "us-west1": 0.01005,
	      "us-west2": 0.01207,
	      "us-west3": 0.01207,
	      "asia-east": 0.01164,
	      "asia-northeast2": 0,
	      "asia-northeast3": 0,
	      "asia-northeast1": 0.01289,
	      "asia-southeast": 0.0124,
	      "asia-southeast1": 0.0124,
	      "europe-west2": 0.01295,
	      "europe-west3": 0.01295,
	      "us-east4": 0.01132,
	      "us-west4": 0.01132,
	      "europe-west1": 0.01106,
	      "europe-west6": 0,
	      "europe-west4": 0.01107,
	      "us-east1": 0.01005,
	      "northamerica-northeast1": 0.01107,
	      "southamerica-east1": 0.01596,
	      "cores": "1",
	      "memory": "4",
	      "asia-southeast2": 0.013516
	    },
	    'f1-micro':{
	      "us": 0.0035,
	      "us-central1": 0.0035,
	      "us-east1": 0.0035,
	      "us-east4": 0.00375,
	      "us-west4": 0.00375,
	      "us-west1": 0.0035,
	      "us-west2": 0.0042,
	      "us-west3": 0.0042,
	      "europe": 0.0039,
	      "europe-west1": 0.0039,
	      "europe-west2": 0.0042,
	      "europe-west3": 0.0042,
	      "europe-west4": 0.0039,
	      "europe-west6": 0.0049,
	      "europe-north1": 0.0039,
	      "northamerica-northeast1": 0.0039,
	      "asia": 0.0039,
	      "asia-east": 0.0039,
	      "asia-east1": 0.0039,
	      "asia-east2": 0.0049,
	      "asia-northeast": 0.005,
	      "asia-northeast1": 0.005,
	      "asia-northeast2": 0.005,
	      "asia-northeast3": 0.005,
	      "asia-southeast": 0.004,
	      "asia-southeast1": 0.004,
	      "australia-southeast1": 0.0046,
	      "australia": 0.0046,
	      "southamerica-east1": 0.0052,
	      "asia-south1": 0.0042,
	      "cores": "shared",
	      "memory": "0.6",
	      "ssd": [
	        0
	      ],
	      "asia-southeast2": 0.00436
	    },
	    'g1-small':{
	      "us": 0.007,
	      "us-central1": 0.007,
	      "us-east1": 0.007,
	      "us-east4": 0.00749,
	      "us-west4": 0.00749,
	      "us-west1": 0.007,
	      "us-west2": 0.0084,
	      "us-west3": 0.0084,
	      "europe": 0.0077,
	      "europe-west1": 0.0077,
	      "europe-west2": 0.0084,
	      "europe-west3": 0.0084,
	      "europe-west4": 0.0077,
	      "europe-west6": 0.0098,
	      "europe-north1": 0.0077,
	      "northamerica-northeast1": 0.0077,
	      "asia": 0.0077,
	      "asia-east": 0.0077,
	      "asia-east1": 0.0077,
	      "asia-east2": 0.0098,
	      "asia-northeast": 0.01,
	      "asia-northeast1": 0.01,
	      "asia-northeast2": 0.01,
	      "asia-northeast3": 0.01,
	      "asia-southeast": 0.0081,
	      "asia-southeast1": 0.0081,
	      "australia-southeast1": 0.0093,
	      "australia": 0.0093,
	      "southamerica-east1": 0.0104,
	      "asia-south1": 0.0084,
	      "cores": "shared",
	      "memory": "1.7",
	      "ssd": [
	        0
	      ],
	      "asia-southeast2": 0.008829
	    },
	},
}


persistentdisk_ratecard = {
  'snapshot': {
      "us": 0.026,
      "us-central1": 0.026,
      "us-east1": 0.026,
      "us-east4": 0.029,
      "us-west4": 0.029,
      "us-west1": 0.026,
      "us-west2": 0.031,
      "us-west3": 0.031,
      "europe": 0.026,
      "europe-west1": 0.026,
      "europe-west2": 0.031,
      "europe-west3": 0.031,
      "europe-west4": 0.029,
      "europe-west6": 0.034,
      "europe-north1": 0.029,
      "northamerica-northeast1": 0.029,
      "asia-east": 0.026,
      "asia-east1": 0.026,
      "asia-east2": 0.032,
      "asia-northeast": 0.034,
      "asia-northeast1": 0.034,
      "asia-northeast2": 0.034,
      "asia-northeast3": 0.034,
      "asia-southeast": 0.029,
      "asia-southeast1": 0.029,
      "australia-southeast1": 0.035,
      "australia": 0.035,
      "southamerica-east1": 0.039,
      "asia-south1": 0.031,
      "asia-southeast2": 0.034
    },
  'gp2': {
      "us": 0.1,
      "us-central1": 0.1,
      "us-east1": 0.1,
      "us-east4": 0.11,
      "us-west4": 0.11,
      "us-west1": 0.1,
      "us-west2": 0.12,
      "us-west3": 0.12,
      "europe": 0.1,
      "europe-west1": 0.1,
      "europe-west2": 0.12,
      "europe-west3": 0.12,
      "europe-west4": 0.11,
      "europe-west6": 0.12,
      "europe-north1": 0.11,
      "northamerica-northeast1": 0.11,
      "asia-east": 0.1,
      "asia-east1": 0.1,
      "asia-east2": 0.11,
      "asia-northeast": 0.13,
      "asia-northeast1": 0.13,
      "asia-northeast2": 0.13,
      "asia-northeast3": 0.13,
      "asia-southeast": 0.11,
      "asia-southeast1": 0.11,
      "australia-southeast1": 0.135,
      "australia": 0.135,
      "southamerica-east1": 0.15,
      "asia-south1": 0.12,
      "asia-southeast2": 0.13,
    },
  'magnetic': {
      "us": 0.04,
      "us-central1": 0.04,
      "us-east1": 0.04,
      "us-east4": 0.044,
      "us-west4": 0.044,
      "us-west1": 0.04,
      "us-west2": 0.048,
      "us-west3": 0.048,
      "europe": 0.04,
      "europe-west1": 0.04,
      "europe-west2": 0.048,
      "europe-west3": 0.048,
      "europe-west4": 0.044,
      "europe-west6": 0.052,
      "europe-north1": 0.044,
      "northamerica-northeast1": 0.044,
      "asia-east": 0.04,
      "asia-east1": 0.04,
      "asia-east2": 0.05,
      "asia-northeast": 0.052,
      "asia-northeast1": 0.052,
      "asia-northeast2": 0.052,
      "asia-northeast3": 0.052,
      "asia-southeast": 0.044,
      "asia-southeast1": 0.044,
      "australia-southeast1": 0.054,
      "australia": 0.054,
      "southamerica-east1": 0.06,
      "asia-south1": 0.048,
      "asia-southeast2": 0.052
    },
}