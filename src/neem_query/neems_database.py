# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Index, String, Text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Neem(Base):
    __tablename__ = 'neems'

    ID = Column(INTEGER(11), primary_key=True)
    _id = Column(String(24), unique=True)
    description = Column(String(255))
    image = Column(Text)
    name = Column(String(255))
    url = Column(String(255))
    created_at = Column(String(255))
    created_by = Column(String(255))
    visibility = Column(TINYINT(1))
    repo = Column(String(255))


class NeemsActivity(Base):
    __tablename__ = 'neems_activity'

    ID = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    url = Column(String(255))


class NeemsProject(Base):
    __tablename__ = 'neems_projects'

    ID = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    url = Column(String(255))


class TfHeader(Base):
    __tablename__ = 'tf_header'

    ID = Column(INTEGER(11), primary_key=True)
    seq = Column(INTEGER(11))
    stamp = Column(Float(asdecimal=True))
    frame_id = Column(String(255))


class TransformRotation(Base):
    __tablename__ = 'transform_rotation'

    ID = Column(INTEGER(11), primary_key=True)
    x = Column(Float(asdecimal=True))
    y = Column(Float(asdecimal=True))
    z = Column(Float(asdecimal=True))
    w = Column(Float(asdecimal=True))


class TransformTranslation(Base):
    __tablename__ = 'transform_translation'

    ID = Column(INTEGER(11), primary_key=True)
    x = Column(Float(asdecimal=True))
    y = Column(Float(asdecimal=True))
    z = Column(Float(asdecimal=True))


class DUL1IsRealizedBy(Base):
    __tablename__ = 'DUL1_isRealizedBy'
    __table_args__ = (
        Index('unique_cols_DUL1_isRealizedBy', 'o', 'DUL1_InformationObject_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    DUL1_InformationObject_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SOMAOBJHasJointPositionMax(Base):
    __tablename__ = 'SOMA_OBJ_hasJointPositionMax'
    __table_args__ = (
        Index('unique_cols_SOMA_OBJ_hasJointPositionMax', 'o', 'SOMA_OBJ_JointLimit_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    SOMA_OBJ_JointLimit_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SOMAOBJHasJointPositionMin(Base):
    __tablename__ = 'SOMA_OBJ_hasJointPositionMin'
    __table_args__ = (
        Index('unique_cols_SOMA_OBJ_hasJointPositionMin', 'o', 'SOMA_OBJ_JointLimit_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    SOMA_OBJ_JointLimit_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SpecificationMetadataCopyright(Base):
    __tablename__ = 'SpecificationMetadata_copyright'

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(Text)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DcmiCreator(Base):
    __tablename__ = 'dcmi_creator'
    __table_args__ = (
        Index('unique_cols_dcmi_creator', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DcmiDate(Base):
    __tablename__ = 'dcmi_date'
    __table_args__ = (
        Index('unique_cols_dcmi_date', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DcmiDescription(Base):
    __tablename__ = 'dcmi_description'

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(Text)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DcmiFormat(Base):
    __tablename__ = 'dcmi_format'
    __table_args__ = (
        Index('unique_cols_dcmi_format', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DcmiIdentifier(Base):
    __tablename__ = 'dcmi_identifier'
    __table_args__ = (
        Index('unique_cols_dcmi_identifier', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DcmiLanguage(Base):
    __tablename__ = 'dcmi_language'
    __table_args__ = (
        Index('unique_cols_dcmi_language', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DcmiPublisher(Base):
    __tablename__ = 'dcmi_publisher'
    __table_args__ = (
        Index('unique_cols_dcmi_publisher', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DcmiSubject(Base):
    __tablename__ = 'dcmi_subject'
    __table_args__ = (
        Index('unique_cols_dcmi_subject', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DcmiTitle(Base):
    __tablename__ = 'dcmi_title'
    __table_args__ = (
        Index('unique_cols_dcmi_title', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DmMarketLeftMarker(Base):
    __tablename__ = 'dm_market_leftMarker'
    __table_args__ = (
        Index('unique_cols_dm_market_leftMarker', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DmMarketMarkerId(Base):
    __tablename__ = 'dm_market_markerId'
    __table_args__ = (
        Index('unique_cols_dm_market_markerId', 'o', 'dm_market_DMShelfMarker_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    dm_market_DMShelfMarker_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DmMarketRightMarker(Base):
    __tablename__ = 'dm_market_rightMarker'
    __table_args__ = (
        Index('unique_cols_dm_market_rightMarker', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulClassify(Base):
    __tablename__ = 'dul_classifies'
    __table_args__ = (
        Index('unique_cols_dul_classifies', 'dul_Concept_s', 'dul_Entity_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Concept_s = Column(String(255), index=True)
    dul_Entity_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulDefine(Base):
    __tablename__ = 'dul_defines'
    __table_args__ = (
        Index('unique_cols_dul_defines', 'dul_Description_s', 'dul_Concept_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Description_s = Column(String(255), index=True)
    dul_Concept_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulDefinesTask(Base):
    __tablename__ = 'dul_definesTask'
    __table_args__ = (
        Index('unique_cols_dul_definesTask', 'dul_Description_s', 'dul_Task_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Description_s = Column(String(255), index=True)
    dul_Task_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulExecutesTask(Base):
    __tablename__ = 'dul_executesTask'
    __table_args__ = (
        Index('unique_cols_dul_executesTask', 'dul_Action_s', 'dul_Task_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Action_s = Column(String(255), index=True)
    dul_Task_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasComponent(Base):
    __tablename__ = 'dul_hasComponent'
    __table_args__ = (
        Index('unique_cols_dul_hasComponent', 'dul_Entity_s', 'dul_Entity_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Entity_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasConstituent(Base):
    __tablename__ = 'dul_hasConstituent'
    __table_args__ = (
        Index('unique_cols_dul_hasConstituent', 'dul_Entity_s', 'dul_Entity_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Entity_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasLocation(Base):
    __tablename__ = 'dul_hasLocation'
    __table_args__ = (
        Index('unique_cols_dul_hasLocation', 'dul_Entity_s', 'dul_Entity_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Entity_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasParameter(Base):
    __tablename__ = 'dul_hasParameter'
    __table_args__ = (
        Index('unique_cols_dul_hasParameter', 'dul_Concept_s', 'dul_Parameter_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Concept_s = Column(String(255), index=True)
    dul_Parameter_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasPart(Base):
    __tablename__ = 'dul_hasPart'
    __table_args__ = (
        Index('unique_cols_dul_hasPart', 'dul_Entity_s', 'dul_Entity_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Entity_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasParticipant(Base):
    __tablename__ = 'dul_hasParticipant'
    __table_args__ = (
        Index('unique_cols_dul_hasParticipant', 'dul_Event_s', 'dul_Object_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Event_s = Column(String(255), index=True)
    dul_Object_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasQuality(Base):
    __tablename__ = 'dul_hasQuality'
    __table_args__ = (
        Index('unique_cols_dul_hasQuality', 'dul_Entity_s', 'dul_Quality_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Quality_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasRegion(Base):
    __tablename__ = 'dul_hasRegion'
    __table_args__ = (
        Index('unique_cols_dul_hasRegion', 'dul_Entity_s', 'dul_Region_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Region_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasRole(Base):
    __tablename__ = 'dul_hasRole'
    __table_args__ = (
        Index('unique_cols_dul_hasRole', 'dul_Object_s', 'dul_Role_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Object_s = Column(String(255), index=True)
    dul_Role_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulHasTimeInterval(Base):
    __tablename__ = 'dul_hasTimeInterval'
    __table_args__ = (
        Index('unique_cols_dul_hasTimeInterval', 'dul_Event_s', 'dul_TimeInterval_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Event_s = Column(String(255), index=True)
    dul_TimeInterval_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulIncludesAction(Base):
    __tablename__ = 'dul_includesAction'
    __table_args__ = (
        Index('unique_cols_dul_includesAction', 'dul_Situation_s', 'dul_Action_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Situation_s = Column(String(255), index=True)
    dul_Action_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulIncludesAgent(Base):
    __tablename__ = 'dul_includesAgent'
    __table_args__ = (
        Index('unique_cols_dul_includesAgent', 'dul_Situation_s', 'dul_Agent_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Situation_s = Column(String(255), index=True)
    dul_Agent_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulIncludesObject(Base):
    __tablename__ = 'dul_includesObject'
    __table_args__ = (
        Index('unique_cols_dul_includesObject', 'dul_Situation_s', 'dul_Object_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Situation_s = Column(String(255), index=True)
    dul_Object_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulIsAbout(Base):
    __tablename__ = 'dul_isAbout'
    __table_args__ = (
        Index('unique_cols_dul_isAbout', 'dul_InformationObject_s', 'dul_Entity_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_InformationObject_s = Column(String(255), index=True)
    dul_Entity_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulIsClassifiedBy(Base):
    __tablename__ = 'dul_isClassifiedBy'
    __table_args__ = (
        Index('unique_cols_dul_isClassifiedBy', 'dul_Entity_s', 'dul_Concept_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Concept_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulIsDescribedBy(Base):
    __tablename__ = 'dul_isDescribedBy'
    __table_args__ = (
        Index('unique_cols_dul_isDescribedBy', 'dul_Entity_s', 'dul_Description_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Description_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulIsSettingFor(Base):
    __tablename__ = 'dul_isSettingFor'
    __table_args__ = (
        Index('unique_cols_dul_isSettingFor', 'dul_Situation_s', 'dul_Entity_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Situation_s = Column(String(255), index=True)
    dul_Entity_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulIsTaskOf(Base):
    __tablename__ = 'dul_isTaskOf'
    __table_args__ = (
        Index('unique_cols_dul_isTaskOf', 'dul_Task_s', 'dul_Role_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Task_s = Column(String(255), index=True)
    dul_Role_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulPrecede(Base):
    __tablename__ = 'dul_precedes'
    __table_args__ = (
        Index('unique_cols_dul_precedes', 'dul_Entity_s', 'dul_Entity_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Entity_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulRealize(Base):
    __tablename__ = 'dul_realizes'
    __table_args__ = (
        Index('unique_cols_dul_realizes', 'dul_InformationRealization_s', 'dul_InformationObject_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_InformationRealization_s = Column(String(255), index=True)
    dul_InformationObject_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulSatisfy(Base):
    __tablename__ = 'dul_satisfies'
    __table_args__ = (
        Index('unique_cols_dul_satisfies', 'dul_Situation_s', 'dul_Description_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Situation_s = Column(String(255), index=True)
    dul_Description_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class DulUsesConcept(Base):
    __tablename__ = 'dul_usesConcept'
    __table_args__ = (
        Index('unique_cols_dul_usesConcept', 'dul_Description_s', 'dul_Concept_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Description_s = Column(String(255), index=True)
    dul_Concept_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class Inferred(Base):
    __tablename__ = 'inferred'

    ID = Column(INTEGER(11), primary_key=True)
    _id = Column(String(24))
    query = Column(String(255))
    module = Column(String(255))
    predicate = Column(String(255))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobDepthOfObject(Base):
    __tablename__ = 'knowrob_depthOfObject'
    __table_args__ = (
        Index('unique_cols_knowrob_depthOfObject', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(Float(asdecimal=True))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobFrameName(Base):
    __tablename__ = 'knowrob_frameName'
    __table_args__ = (
        Index('unique_cols_knowrob_frameName', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobHasLifetime(Base):
    __tablename__ = 'knowrob_hasLifetime'
    __table_args__ = (
        Index('unique_cols_knowrob_hasLifetime', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobHasVisual(Base):
    __tablename__ = 'knowrob_hasVisual'
    __table_args__ = (
        Index('unique_cols_knowrob_hasVisual', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(TINYINT(1))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobHeightOfObject(Base):
    __tablename__ = 'knowrob_heightOfObject'
    __table_args__ = (
        Index('unique_cols_knowrob_heightOfObject', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(Float(asdecimal=True))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobQuaternion(Base):
    __tablename__ = 'knowrob_quaternion'
    __table_args__ = (
        Index('unique_cols_knowrob_quaternion', 's', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobTodo(Base):
    __tablename__ = 'knowrob_todo'
    __table_args__ = (
        Index('unique_cols_knowrob_todo', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobTranslation(Base):
    __tablename__ = 'knowrob_translation'
    __table_args__ = (
        Index('unique_cols_knowrob_translation', 's', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobWidthOfObject(Base):
    __tablename__ = 'knowrob_widthOfObject'
    __table_args__ = (
        Index('unique_cols_knowrob_widthOfObject', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(Float(asdecimal=True))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class LinkFoodOnIntersectionOf(Base):
    __tablename__ = 'linkFoodOn_intersectionOf'
    __table_args__ = (
        Index('unique_cols_linkFoodOn_intersectionOf', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class LinkFoodOnOnProperty(Base):
    __tablename__ = 'linkFoodOn_onProperty'
    __table_args__ = (
        Index('unique_cols_linkFoodOn_onProperty', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class LinkFoodOnSomeValuesFrom(Base):
    __tablename__ = 'linkFoodOn_someValuesFrom'
    __table_args__ = (
        Index('unique_cols_linkFoodOn_someValuesFrom', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class NeemsActivityIndex(Base):
    __tablename__ = 'neems_activity_index'

    ID = Column(INTEGER(11), primary_key=True)
    neems_ID = Column(ForeignKey('neems.ID', ondelete='CASCADE'), index=True)
    list_index = Column(INTEGER(11))
    neems_activity_ID = Column(ForeignKey('neems_activity.ID', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')
    neems_activity = relationship('NeemsActivity')


class NeemsAgentIndex(Base):
    __tablename__ = 'neems_agent_index'

    ID = Column(INTEGER(11), primary_key=True)
    neems_ID = Column(ForeignKey('neems.ID', ondelete='CASCADE'), index=True)
    list_index = Column(INTEGER(11))
    agent_values = Column(String(255))

    neem = relationship('Neem')


class NeemsEnvironmentIndex(Base):
    __tablename__ = 'neems_environment_index'

    ID = Column(INTEGER(11), primary_key=True)
    neems_ID = Column(ForeignKey('neems.ID', ondelete='CASCADE'), index=True)
    list_index = Column(INTEGER(11))
    environment_values = Column(String(255))

    neem = relationship('Neem')


class NeemsKeywordsIndex(Base):
    __tablename__ = 'neems_keywords_index'

    ID = Column(INTEGER(11), primary_key=True)
    neems_ID = Column(ForeignKey('neems.ID', ondelete='CASCADE'), index=True)
    list_index = Column(INTEGER(11))
    keywords_values = Column(String(255))

    neem = relationship('Neem')


class NeemsMailIndex(Base):
    __tablename__ = 'neems_mail_index'

    ID = Column(INTEGER(11), primary_key=True)
    neems_ID = Column(ForeignKey('neems.ID', ondelete='CASCADE'), index=True)
    list_index = Column(INTEGER(11))
    mail_values = Column(String(255))

    neem = relationship('Neem')


class NeemsModelVersionIndex(Base):
    __tablename__ = 'neems_model_version_index'

    ID = Column(INTEGER(11), primary_key=True)
    neems_ID = Column(ForeignKey('neems.ID', ondelete='CASCADE'), index=True)
    list_index = Column(INTEGER(11))
    model_version_values = Column(String(255))

    neem = relationship('Neem')


class NeemsProjectsIndex(Base):
    __tablename__ = 'neems_projects_index'

    ID = Column(INTEGER(11), primary_key=True)
    neems_ID = Column(ForeignKey('neems.ID', ondelete='CASCADE'), index=True)
    list_index = Column(INTEGER(11))
    neems_projects_ID = Column(ForeignKey('neems_projects.ID', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')
    neems_project = relationship('NeemsProject')


class OboInOwlHasBroadSynonym(Base):
    __tablename__ = 'oboInOwl_hasBroadSynonym'
    __table_args__ = (
        Index('unique_cols_oboInOwl_hasBroadSynonym', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OboInOwlHasDbXref(Base):
    __tablename__ = 'oboInOwl_hasDbXref'
    __table_args__ = (
        Index('unique_cols_oboInOwl_hasDbXref', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OboInOwlHasExactSynonym(Base):
    __tablename__ = 'oboInOwl_hasExactSynonym'
    __table_args__ = (
        Index('unique_cols_oboInOwl_hasExactSynonym', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OboInOwlHasSynonym(Base):
    __tablename__ = 'oboInOwl_hasSynonym'
    __table_args__ = (
        Index('unique_cols_oboInOwl_hasSynonym', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OboInOwlInSubset(Base):
    __tablename__ = 'oboInOwl_inSubset'
    __table_args__ = (
        Index('unique_cols_oboInOwl_inSubset', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlAllValuesFrom(Base):
    __tablename__ = 'owl_allValuesFrom'
    __table_args__ = (
        Index('unique_cols_owl_allValuesFrom', 'owl_Restriction_s', 'rdfs_Class_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_Restriction_s = Column(String(255), index=True)
    rdfs_Class_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlAnnotatedProperty(Base):
    __tablename__ = 'owl_annotatedProperty'
    __table_args__ = (
        Index('unique_cols_owl_annotatedProperty', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlAnnotatedSource(Base):
    __tablename__ = 'owl_annotatedSource'
    __table_args__ = (
        Index('unique_cols_owl_annotatedSource', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlAnnotatedTarget(Base):
    __tablename__ = 'owl_annotatedTarget'
    __table_args__ = (
        Index('unique_cols_owl_annotatedTarget', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlCardinality(Base):
    __tablename__ = 'owl_cardinality'
    __table_args__ = (
        Index('unique_cols_owl_cardinality', 'o', 'owl_Restriction_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(INTEGER(11))
    owl_Restriction_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlComplementOf(Base):
    __tablename__ = 'owl_complementOf'
    __table_args__ = (
        Index('unique_cols_owl_complementOf', 'owl_Class_s', 'owl_Class_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_Class_s = Column(String(255), index=True)
    owl_Class_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlDisjointWith(Base):
    __tablename__ = 'owl_disjointWith'
    __table_args__ = (
        Index('unique_cols_owl_disjointWith', 'owl_Class_s', 'owl_Class_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_Class_s = Column(String(255), index=True)
    owl_Class_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlEquivalentClas(Base):
    __tablename__ = 'owl_equivalentClass'
    __table_args__ = (
        Index('unique_cols_owl_equivalentClass', 'owl_Class_s', 'owl_Class_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_Class_s = Column(String(255), index=True)
    owl_Class_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlHasKey(Base):
    __tablename__ = 'owl_hasKey'
    __table_args__ = (
        Index('unique_cols_owl_hasKey', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlHasSelf(Base):
    __tablename__ = 'owl_hasSelf'
    __table_args__ = (
        Index('unique_cols_owl_hasSelf', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(TINYINT(1))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlHasValue(Base):
    __tablename__ = 'owl_hasValue'
    __table_args__ = (
        Index('unique_cols_owl_hasValue', 'o', 'owl_Restriction_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    owl_Restriction_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlImport(Base):
    __tablename__ = 'owl_imports'
    __table_args__ = (
        Index('unique_cols_owl_imports', 'owl_Ontology_s', 'owl_Ontology_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_Ontology_s = Column(String(255), index=True)
    owl_Ontology_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlIntersectionOf(Base):
    __tablename__ = 'owl_intersectionOf'
    __table_args__ = (
        Index('unique_cols_owl_intersectionOf', 'owl_Class_s', 'rdf_List_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_Class_s = Column(String(255), index=True)
    rdf_List_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlInverseOf(Base):
    __tablename__ = 'owl_inverseOf'
    __table_args__ = (
        Index('unique_cols_owl_inverseOf', 'owl_ObjectProperty_s', 'owl_ObjectProperty_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_ObjectProperty_s = Column(String(255), index=True)
    owl_ObjectProperty_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlMaxQualifiedCardinality(Base):
    __tablename__ = 'owl_maxQualifiedCardinality'
    __table_args__ = (
        Index('unique_cols_owl_maxQualifiedCardinality', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(INTEGER(11))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlMember(Base):
    __tablename__ = 'owl_members'
    __table_args__ = (
        Index('unique_cols_owl_members', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlMinCardinality(Base):
    __tablename__ = 'owl_minCardinality'
    __table_args__ = (
        Index('unique_cols_owl_minCardinality', 'o', 'owl_Restriction_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(INTEGER(11))
    owl_Restriction_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlMinQualifiedCardinality(Base):
    __tablename__ = 'owl_minQualifiedCardinality'
    __table_args__ = (
        Index('unique_cols_owl_minQualifiedCardinality', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(Float(asdecimal=True))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlOnClas(Base):
    __tablename__ = 'owl_onClass'
    __table_args__ = (
        Index('unique_cols_owl_onClass', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlOnDataRange(Base):
    __tablename__ = 'owl_onDataRange'
    __table_args__ = (
        Index('unique_cols_owl_onDataRange', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlOnProperty(Base):
    __tablename__ = 'owl_onProperty'
    __table_args__ = (
        Index('unique_cols_owl_onProperty', 'owl_Restriction_s', 'rdf_Property_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_Restriction_s = Column(String(255), index=True)
    rdf_Property_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlOneOf(Base):
    __tablename__ = 'owl_oneOf'
    __table_args__ = (
        Index('unique_cols_owl_oneOf', 'rdfs_Class_s', 'rdf_List_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    rdfs_Class_s = Column(String(255), index=True)
    rdf_List_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlPropertyChainAxiom(Base):
    __tablename__ = 'owl_propertyChainAxiom'
    __table_args__ = (
        Index('unique_cols_owl_propertyChainAxiom', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlQualifiedCardinality(Base):
    __tablename__ = 'owl_qualifiedCardinality'
    __table_args__ = (
        Index('unique_cols_owl_qualifiedCardinality', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(INTEGER(11))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlSameA(Base):
    __tablename__ = 'owl_sameAs'
    __table_args__ = (
        Index('unique_cols_owl_sameAs', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlSomeValuesFrom(Base):
    __tablename__ = 'owl_someValuesFrom'
    __table_args__ = (
        Index('unique_cols_owl_someValuesFrom', 'owl_Restriction_s', 'rdfs_Class_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_Restriction_s = Column(String(255), index=True)
    rdfs_Class_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlUnionOf(Base):
    __tablename__ = 'owl_unionOf'
    __table_args__ = (
        Index('unique_cols_owl_unionOf', 'owl_Class_s', 'rdf_List_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    owl_Class_s = Column(String(255), index=True)
    rdf_List_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlVersionIRI(Base):
    __tablename__ = 'owl_versionIRI'
    __table_args__ = (
        Index('unique_cols_owl_versionIRI', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class OwlVersionInfo(Base):
    __tablename__ = 'owl_versionInfo'

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(Text)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ProductTaxonomyHasDAN(Base):
    __tablename__ = 'product_taxonomy_has_DAN'
    __table_args__ = (
        Index('unique_cols_product_taxonomy_has_DAN', 'o', 'v1_ProductOrService_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    v1_ProductOrService_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfFirst(Base):
    __tablename__ = 'rdf_first'
    __table_args__ = (
        Index('unique_cols_rdf_first', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfRest(Base):
    __tablename__ = 'rdf_rest'
    __table_args__ = (
        Index('unique_cols_rdf_rest', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfType(Base):
    __tablename__ = 'rdf_type'
    __table_args__ = (
        Index('unique_cols_rdf_type', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfsComment(Base):
    __tablename__ = 'rdfs_comment'

    ID = Column(INTEGER(11), primary_key=True)
    rdfs_Resource_s = Column(String(255), index=True)
    rdfs_Literal_o = Column(Text)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfsDomain(Base):
    __tablename__ = 'rdfs_domain'
    __table_args__ = (
        Index('unique_cols_rdfs_domain', 'rdf_Property_s', 'rdfs_Class_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    rdf_Property_s = Column(String(255), index=True)
    rdfs_Class_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfsIsDefinedBy(Base):
    __tablename__ = 'rdfs_isDefinedBy'
    __table_args__ = (
        Index('unique_cols_rdfs_isDefinedBy', 'rdfs_Resource_s', 'rdfs_Resource_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    rdfs_Resource_s = Column(String(255), index=True)
    rdfs_Resource_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfsLabel(Base):
    __tablename__ = 'rdfs_label'

    ID = Column(INTEGER(11), primary_key=True)
    rdfs_Resource_s = Column(String(255), index=True)
    rdfs_Literal_o = Column(Text)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfsRange(Base):
    __tablename__ = 'rdfs_range'
    __table_args__ = (
        Index('unique_cols_rdfs_range', 'rdf_Property_s', 'rdfs_Class_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    rdf_Property_s = Column(String(255), index=True)
    rdfs_Class_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfsSeeAlso(Base):
    __tablename__ = 'rdfs_seeAlso'

    ID = Column(INTEGER(11), primary_key=True)
    rdfs_Resource_s = Column(String(255), index=True)
    rdfs_Resource_o = Column(Text)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfsSubClassOf(Base):
    __tablename__ = 'rdfs_subClassOf'
    __table_args__ = (
        Index('unique_cols_rdfs_subClassOf', 'rdfs_Class_s', 'rdfs_Class_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    rdfs_Class_s = Column(String(255), index=True)
    rdfs_Class_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class RdfsSubPropertyOf(Base):
    __tablename__ = 'rdfs_subPropertyOf'
    __table_args__ = (
        Index('unique_cols_rdfs_subPropertyOf', 'rdf_Property_s', 'rdf_Property_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    rdf_Property_s = Column(String(255), index=True)
    rdf_Property_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopAdjacentLabelOfFacing(Base):
    __tablename__ = 'shop_adjacentLabelOfFacing'
    __table_args__ = (
        Index('unique_cols_shop_adjacentLabelOfFacing', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopArticleNumberOfLabel(Base):
    __tablename__ = 'shop_articleNumberOfLabel'
    __table_args__ = (
        Index('unique_cols_shop_articleNumberOfLabel', 'o', 'shop_ShelfLabel_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    shop_ShelfLabel_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopDan(Base):
    __tablename__ = 'shop_dan'
    __table_args__ = (
        Index('unique_cols_shop_dan', 'o', 'shop_ArticleNumber_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    shop_ArticleNumber_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopGtin(Base):
    __tablename__ = 'shop_gtin'
    __table_args__ = (
        Index('unique_cols_shop_gtin', 'o', 'shop_ArticleNumber_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    shop_ArticleNumber_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopLabelOfFacing(Base):
    __tablename__ = 'shop_labelOfFacing'
    __table_args__ = (
        Index('unique_cols_shop_labelOfFacing', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopLayerOfFacing(Base):
    __tablename__ = 'shop_layerOfFacing'
    __table_args__ = (
        Index('unique_cols_shop_layerOfFacing', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopLeftSeparator(Base):
    __tablename__ = 'shop_leftSeparator'
    __table_args__ = (
        Index('unique_cols_shop_leftSeparator', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopPreferredLabelOfFacing(Base):
    __tablename__ = 'shop_preferredLabelOfFacing'
    __table_args__ = (
        Index('unique_cols_shop_preferredLabelOfFacing', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopProductInFacing(Base):
    __tablename__ = 'shop_productInFacing'
    __table_args__ = (
        Index('unique_cols_shop_productInFacing', 's', 'shop_Product_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    shop_Product_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopProductLabelOfFacing(Base):
    __tablename__ = 'shop_productLabelOfFacing'
    __table_args__ = (
        Index('unique_cols_shop_productLabelOfFacing', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class ShopRightSeparator(Base):
    __tablename__ = 'shop_rightSeparator'
    __table_args__ = (
        Index('unique_cols_shop_rightSeparator', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaUsageGuideline(Base):
    __tablename__ = 'soma_UsageGuideline'

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(Text)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaContain(Base):
    __tablename__ = 'soma_contains'
    __table_args__ = (
        Index('unique_cols_soma_contains', 'dul_Entity_s', 'dul_Entity_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Entity_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaDefinesBearer(Base):
    __tablename__ = 'soma_definesBearer'
    __table_args__ = (
        Index('unique_cols_soma_definesBearer', 'soma_Affordance_s', 'dul_Role_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    soma_Affordance_s = Column(String(255), index=True)
    dul_Role_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaDefinesTrigger(Base):
    __tablename__ = 'soma_definesTrigger'
    __table_args__ = (
        Index('unique_cols_soma_definesTrigger', 'soma_Affordance_s', 'dul_Role_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    soma_Affordance_s = Column(String(255), index=True)
    dul_Role_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaFinishedBy(Base):
    __tablename__ = 'soma_finishedBy'
    __table_args__ = (
        Index('unique_cols_soma_finishedBy', 'dul_Event_s', 'dul_Event_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Event_s = Column(String(255), index=True)
    dul_Event_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasColor(Base):
    __tablename__ = 'soma_hasColor'
    __table_args__ = (
        Index('unique_cols_soma_hasColor', 'dul_PhysicalObject_s', 'soma_Color_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    soma_Color_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasDataFormat(Base):
    __tablename__ = 'soma_hasDataFormat'
    __table_args__ = (
        Index('unique_cols_soma_hasDataFormat', 'o', 'dul_InformationRealization_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    dul_InformationRealization_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasDepth(Base):
    __tablename__ = 'soma_hasDepth'
    __table_args__ = (
        Index('unique_cols_soma_hasDepth', 'o', 'soma_ShapeRegion_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    soma_ShapeRegion_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasDisposition(Base):
    __tablename__ = 'soma_hasDisposition'
    __table_args__ = (
        Index('unique_cols_soma_hasDisposition', 'dul_Object_s', 'soma_Disposition_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Object_s = Column(String(255), index=True)
    soma_Disposition_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasExecutionState(Base):
    __tablename__ = 'soma_hasExecutionState'
    __table_args__ = (
        Index('unique_cols_soma_hasExecutionState', 'dul_Action_s', 'soma_ExecutionStateRegion_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Action_s = Column(String(255), index=True)
    soma_ExecutionStateRegion_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasFeature(Base):
    __tablename__ = 'soma_hasFeature'
    __table_args__ = (
        Index('unique_cols_soma_hasFeature', 'dul_PhysicalObject_s', 'soma_Feature_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    soma_Feature_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasFilePath(Base):
    __tablename__ = 'soma_hasFilePath'
    __table_args__ = (
        Index('unique_cols_soma_hasFilePath', 'o', 'dul_Entity_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    dul_Entity_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasGoal(Base):
    __tablename__ = 'soma_hasGoal'
    __table_args__ = (
        Index('unique_cols_soma_hasGoal', 'dul_Entity_s', 'dul_Goal_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    dul_Goal_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasHeight(Base):
    __tablename__ = 'soma_hasHeight'
    __table_args__ = (
        Index('unique_cols_soma_hasHeight', 'o', 'soma_ShapeRegion_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    soma_ShapeRegion_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasIntervalBegin(Base):
    __tablename__ = 'soma_hasIntervalBegin'
    __table_args__ = (
        Index('unique_cols_soma_hasIntervalBegin', 'o', 'dul_TimeInterval_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    dul_TimeInterval_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasIntervalEnd(Base):
    __tablename__ = 'soma_hasIntervalEnd'
    __table_args__ = (
        Index('unique_cols_soma_hasIntervalEnd', 'o', 'dul_TimeInterval_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    dul_TimeInterval_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasLocalization(Base):
    __tablename__ = 'soma_hasLocalization'
    __table_args__ = (
        Index('unique_cols_soma_hasLocalization', 'dul_PhysicalObject_s', 'soma_Localization_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    soma_Localization_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasOrientationVector(Base):
    __tablename__ = 'soma_hasOrientationVector'
    __table_args__ = (
        Index('unique_cols_soma_hasOrientationVector', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasPersistentIdentifier(Base):
    __tablename__ = 'soma_hasPersistentIdentifier'
    __table_args__ = (
        Index('unique_cols_soma_hasPersistentIdentifier', 'o', 'dul_InformationRealization_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    dul_InformationRealization_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasPhysicalComponent(Base):
    __tablename__ = 'soma_hasPhysicalComponent'
    __table_args__ = (
        Index('unique_cols_soma_hasPhysicalComponent', 'dul_PhysicalObject_s', 'dul_PhysicalObject_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    dul_PhysicalObject_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasPositionVector(Base):
    __tablename__ = 'soma_hasPositionVector'
    __table_args__ = (
        Index('unique_cols_soma_hasPositionVector', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasRGBValue(Base):
    __tablename__ = 'soma_hasRGBValue'
    __table_args__ = (
        Index('unique_cols_soma_hasRGBValue', 'o', 'soma_ColorRegion_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    soma_ColorRegion_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasShape(Base):
    __tablename__ = 'soma_hasShape'
    __table_args__ = (
        Index('unique_cols_soma_hasShape', 'dul_PhysicalObject_s', 'soma_Shape_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    soma_Shape_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasTransparencyValue(Base):
    __tablename__ = 'soma_hasTransparencyValue'
    __table_args__ = (
        Index('unique_cols_soma_hasTransparencyValue', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(Float(asdecimal=True))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaHasWidth(Base):
    __tablename__ = 'soma_hasWidth'
    __table_args__ = (
        Index('unique_cols_soma_hasWidth', 'o', 'soma_ShapeRegion_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    soma_ShapeRegion_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaIsPerformedBy(Base):
    __tablename__ = 'soma_isPerformedBy'
    __table_args__ = (
        Index('unique_cols_soma_isPerformedBy', 'dul_Action_s', 'dul_Agent_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Action_s = Column(String(255), index=True)
    dul_Agent_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaIsProcessTypeOf(Base):
    __tablename__ = 'soma_isProcessTypeOf'
    __table_args__ = (
        Index('unique_cols_soma_isProcessTypeOf', 'soma_ProcessType_s', 'dul_Role_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    soma_ProcessType_s = Column(String(255), index=True)
    dul_Role_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaIsReificationOf(Base):
    __tablename__ = 'soma_isReificationOf'
    __table_args__ = (
        Index('unique_cols_soma_isReificationOf', 'o', 'dul_Description_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    dul_Description_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaStartedBy(Base):
    __tablename__ = 'soma_startedBy'
    __table_args__ = (
        Index('unique_cols_soma_startedBy', 'dul_Event_s', 'dul_Event_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Event_s = Column(String(255), index=True)
    dul_Event_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class SomaSymbol(Base):
    __tablename__ = 'soma_symbol'
    __table_args__ = (
        Index('unique_cols_soma_symbol', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class Srdl2CapHasCapability(Base):
    __tablename__ = 'srdl2_cap_hasCapability'
    __table_args__ = (
        Index('unique_cols_srdl2_cap_hasCapability', 'dul_Agent_s', 'srdl2_cap_Capability_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Agent_s = Column(String(255), index=True)
    srdl2_cap_Capability_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class Srdl2CompHasBodyPart(Base):
    __tablename__ = 'srdl2_comp_hasBodyPart'
    __table_args__ = (
        Index('unique_cols_srdl2_comp_hasBodyPart', 'dul_PhysicalAgent_s', 'dul_PhysicalObject_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_PhysicalAgent_s = Column(String(255), index=True)
    dul_PhysicalObject_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class Srdl2CompHasGripForceValue(Base):
    __tablename__ = 'srdl2_comp_hasGripForceValue'
    __table_args__ = (
        Index('unique_cols_srdl2_comp_hasGripForceValue', 'o', 'urdf_GripForceAttribute_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    urdf_GripForceAttribute_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class Srdl2CompHasMaximumSpeedValue(Base):
    __tablename__ = 'srdl2_comp_hasMaximumSpeedValue'
    __table_args__ = (
        Index('unique_cols_srdl2_comp_hasMaximumSpeedValue', 'o', 'srdl2_comp_MaximumSpeed_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    srdl2_comp_MaximumSpeed_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class Srdl2CompHasPayloadValue(Base):
    __tablename__ = 'srdl2_comp_hasPayloadValue'
    __table_args__ = (
        Index('unique_cols_srdl2_comp_hasPayloadValue', 'o', 'srdl2_comp_PayloadAttribute_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(Float(asdecimal=True))
    srdl2_comp_PayloadAttribute_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class Srdl2CompSphereInertiaMas(Base):
    __tablename__ = 'srdl2_comp_sphere_inertia_mass'
    __table_args__ = (
        Index('unique_cols_srdl2_comp_sphere_inertia_mass', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class Srdl2CompSphereInertiaRadiu(Base):
    __tablename__ = 'srdl2_comp_sphere_inertia_radius'
    __table_args__ = (
        Index('unique_cols_srdl2_comp_sphere_inertia_radius', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class TermsContributor(Base):
    __tablename__ = 'terms_contributor'
    __table_args__ = (
        Index('unique_cols_terms_contributor', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class TermsLicense(Base):
    __tablename__ = 'terms_license'
    __table_args__ = (
        Index('unique_cols_terms_license', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class TfTransform(Base):
    __tablename__ = 'tf_transform'

    ID = Column(INTEGER(11), primary_key=True)
    translation = Column(ForeignKey('transform_translation.ID', ondelete='CASCADE'), index=True)
    rotation = Column(ForeignKey('transform_rotation.ID', ondelete='CASCADE'), index=True)

    transform_rotation = relationship('TransformRotation')
    transform_translation = relationship('TransformTranslation')


class TripledbVersionString(Base):
    __tablename__ = 'tripledbVersionString'

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class TrustSource(Base):
    __tablename__ = 'trust_source'
    __table_args__ = (
        Index('unique_cols_trust_source', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class TrustWikientry(Base):
    __tablename__ = 'trust_wikientry'
    __table_args__ = (
        Index('unique_cols_trust_wikientry', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class UrdfHasBaseLink(Base):
    __tablename__ = 'urdf_hasBaseLink'
    __table_args__ = (
        Index('unique_cols_urdf_hasBaseLink', 'dul_PhysicalObject_s', 'urdf_Link_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    urdf_Link_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class UrdfHasBaseLinkName(Base):
    __tablename__ = 'urdf_hasBaseLinkName'
    __table_args__ = (
        Index('unique_cols_urdf_hasBaseLinkName', 'o', 'dul_PhysicalObject_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class UrdfHasChildLink(Base):
    __tablename__ = 'urdf_hasChildLink'
    __table_args__ = (
        Index('unique_cols_urdf_hasChildLink', 'urdf_Joint_s', 'dul_PhysicalObject_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    urdf_Joint_s = Column(String(255), index=True)
    dul_PhysicalObject_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class UrdfHasEndLink(Base):
    __tablename__ = 'urdf_hasEndLink'
    __table_args__ = (
        Index('unique_cols_urdf_hasEndLink', 'dul_PhysicalObject_s', 'urdf_Link_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    urdf_Link_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class UrdfHasEndLinkName(Base):
    __tablename__ = 'urdf_hasEndLinkName'
    __table_args__ = (
        Index('unique_cols_urdf_hasEndLinkName', 'o', 'dul_PhysicalObject_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class UrdfHasNamePrefix(Base):
    __tablename__ = 'urdf_hasNamePrefix'
    __table_args__ = (
        Index('unique_cols_urdf_hasNamePrefix', 's', 'o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    s = Column(String(255), index=True)
    o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class UrdfHasOrigin(Base):
    __tablename__ = 'urdf_hasOrigin'
    __table_args__ = (
        Index('unique_cols_urdf_hasOrigin', 'dul_Entity_s', 'soma_6DPose_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    dul_Entity_s = Column(String(255), index=True)
    soma_6DPose_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class UrdfHasParentLink(Base):
    __tablename__ = 'urdf_hasParentLink'
    __table_args__ = (
        Index('unique_cols_urdf_hasParentLink', 'urdf_Joint_s', 'dul_PhysicalObject_o', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    urdf_Joint_s = Column(String(255), index=True)
    dul_PhysicalObject_o = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class UrdfHasURDFName(Base):
    __tablename__ = 'urdf_hasURDFName'
    __table_args__ = (
        Index('unique_cols_urdf_hasURDFName', 'o', 'dul_PhysicalObject_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    dul_PhysicalObject_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class V1HasEANUCC13(Base):
    __tablename__ = 'v1_hasEAN_UCC_13'
    __table_args__ = (
        Index('unique_cols_v1_hasEAN_UCC_13', 'o', 'v1_ProductOrService_s', 'neem_id', unique=True),
    )

    ID = Column(INTEGER(11), primary_key=True)
    o = Column(String(255), index=True)
    v1_ProductOrService_s = Column(String(255), index=True)
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    neem = relationship('Neem')


class KnowrobQuaternionOIndex(Base):
    __tablename__ = 'knowrob_quaternion_o_index'

    ID = Column(INTEGER(11), primary_key=True)
    knowrob_quaternion_ID = Column(ForeignKey('knowrob_quaternion.ID', ondelete='CASCADE'), index=True)
    list_index = Column(INTEGER(11))
    o_values = Column(Float(asdecimal=True))

    knowrob_quaternion = relationship('KnowrobQuaternion')


class KnowrobTranslationOIndex(Base):
    __tablename__ = 'knowrob_translation_o_index'

    ID = Column(INTEGER(11), primary_key=True)
    knowrob_translation_ID = Column(ForeignKey('knowrob_translation.ID', ondelete='CASCADE'), index=True)
    list_index = Column(INTEGER(11))
    o_values = Column(Float(asdecimal=True))

    knowrob_translation = relationship('KnowrobTranslation')


class Tf(Base):
    __tablename__ = 'tf'

    ID = Column(INTEGER(11), primary_key=True)
    _id = Column(String(24))
    header = Column(ForeignKey('tf_header.ID', ondelete='CASCADE'), index=True)
    child_frame_id = Column(String(255))
    transform = Column(ForeignKey('tf_transform.ID', ondelete='CASCADE'), index=True)
    __recorded = Column(Float(asdecimal=True))
    __topic = Column(String(255))
    neem_id = Column(ForeignKey('neems._id', ondelete='CASCADE'), index=True)

    tf_header = relationship('TfHeader')
    neem = relationship('Neem')
    tf_transform = relationship('TfTransform')


class TfHeaderSomaHasIntervalBegin(Base):
    __tablename__ = 'tf_header_soma_hasIntervalBegin'

    ID = Column(INTEGER(11), primary_key=True)
    tf_header_ID = Column(ForeignKey('tf_header.ID', ondelete='CASCADE'), index=True)
    soma_hasIntervalBegin_ID = Column(ForeignKey('soma_hasIntervalBegin.ID', ondelete='CASCADE'), index=True)
    soma_hasIntervalEnd_ID = Column(ForeignKey('soma_hasIntervalEnd.ID', ondelete='CASCADE'), index=True)

    soma_hasIntervalBegin = relationship('SomaHasIntervalBegin')
    soma_hasIntervalEnd = relationship('SomaHasIntervalEnd')
    tf_header = relationship('TfHeader')
