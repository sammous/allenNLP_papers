from typing import Tuple, List

from overrides import overrides

from allennlp.common.util import JsonDict
from allennlp.data import Instance
from allennlp.service.predictors.predictor import Predictor

@Predictor.register('paper-classifier')
class PaperClassifierPredictor(Predictor):
    """"Predictor wrapper for the AcademicPaperClassifier"""
    @overrides
    def _json_to_instance(self, json_dict: JsonDict) -> Tuple[Instance, JsonDict]:
        title = json_dict['title']
        abstract = json_dict['abstract']

        instance = self._dataset_reader.text_to_instance(title=title, abstract=abstract)
        # label_dict will be like {0: "ACL", 1: "AI", ...}
        label_dict = self._model.vocab.get_index_to_token_vocabulary('labels')

        return instance, {"labels": ['health_sciences', 'life_sciences', 'physical_sciences', 'social_sciences']}
